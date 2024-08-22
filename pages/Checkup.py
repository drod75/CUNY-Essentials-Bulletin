import streamlit as st
import pandas as pd
import os

#access text file step 1: account checking
if not(st.session_state.get('authentication_status')):
    st.markdown('# Please Login to use this feature')
else:
    if 'counters' not in st.session_state:
        #read checkup values, auto set to 0 for new accounts in authentication
        checkup_account_data = pd.read_csv('pages\checkup_data\checkup.csv')
        account_read = checkup_account_data.loc[(checkup_account_data['account-name'] == st.session_state['name']) & (checkup_account_data['account-username'] == st.session_state['username'])]
        st.session_state.counters = {
            'happy': account_read['happy-count'],
            'stress': account_read['stress-count'],
            'anxiety': account_read['anxiety-count'],
            'depressed': account_read['depressed-count']
        }
    if 'question_visible' not in st.session_state:
        st.session_state.question_visible = True

    #Display the feeling options and a button to record them
    if st.session_state.question_visible:
        st.header('How are you feeling today?')
        feelings = ['Happy', 'Stress ', 'Anxiety', 'Depressed']
        selected_feeling = st.radio('Select your current feeling:', feelings)

        if st.button('Save Feeling'):
            feeling_key = selected_feeling.lower()
            if feeling_key in st.session_state.counters:
                st.session_state.counters[feeling_key] += 1
                st.success(f'Your feeling "{selected_feeling}" has been recorded.')
                st.session_state.question_visible = False  # Hide the question after recording
    else:
        st.success('Thank you for sharing your feelings!')

    #Display the counters for all feelings
    st.header('Feeling Counts')
    st.write(f"Happy: {st.session_state.counters['happy']}")
    st.write(f"Stress: {st.session_state.counters['stress']}")
    st.write(f"Anxiety: {st.session_state.counters['anxiety']}")
    st.write(f"Depressed: {st.session_state.counters['depressed']}")

    st.title('Personalized Care Setup')

    #User Preferences
    goals = st.multiselect(
        'What are your mental health goals?',
        ['Reducing stress', 'Improving sleep', 'Managing anxiety', 'Enhancing focus']
    )

    activities = st.multiselect(
        'Which activities do you prefer?',
        ['Meditation', 'Physical exercise', 'Breathing exercises']
    )

    time_commitment = st.slider(
        'How much time can you spend daily?',
        min_value=5, max_value=60, step=5
    )

    if st.button('Save Preferences'):
        st.session_state['preferences'] = {
            'goals': goals,
            'activities': activities,
            'time_commitment': time_commitment
        }
        st.write('Preferences saved!')

    #Display saved preferences
    if 'preferences' in st.session_state:
        preferences = st.session_state['preferences']
        st.write('Your preferences:')
        st.write(preferences)

    #save counts to file
    checkup_account_data = pd.read_csv('pages\checkup_data\checkup.csv')
    account_read = checkup_account_data.loc[(checkup_account_data['account-name'] == st.session_state['name']) & (checkup_account_data['account-username'] == st.session_state['username'])]

    account_read['happy-count'] = st.session_state.counters['happy']
    account_read['stress-count'] = st.session_state.counters['stress']
    account_read['anxiety-count'] = st.session_state.counters['anxiety']
    account_read['depressed-count'] = st.session_state.counters['depressed']

    checkup_account_data.loc[(checkup_account_data['account-name'] == st.session_state['name']) & (checkup_account_data['account-username'] == st.session_state['username'])] = account_read
    import os
    path = 'pages\checkup_data\checkup.csv'
    checkup_account_data.to_csv(os.path.join(path,r'checkup.csv'))
    