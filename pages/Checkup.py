import streamlit as st
import pandas as pd

#access text file step 1: account checking
if not(st.session_state.get('authentication_status')):
    st.markdown('# Please Login to use this feature')
else:
    if 'counters' not in st.session_state:
        #read checkup values, auto set to 0 for new accounts in authentication
        ad = pd.read_csv('pages\checkup.csv')
        account_read = ad.loc[(ad['account-name'] == st.session_state['name']) & (ad['account-username'] == st.session_state['username'])]
        st.session_state.counters = {
            'happy': int(account_read['happy-count']),
            'stress': int(account_read['stress-count']),
            'anxiety': int(account_read['anxiety-count']),
            'depressed': int(account_read['depressed-count'])
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
    goals = st.selectbox(
        'What is your mental health goal?',
        ['Reducing stress', 'Improving sleep', 'Managing anxiety', 'Enhancing focus']
    )
    activity = st.selectbox(
        'Which activity do you prefer?',
        ['Meditation', 'Physical exercise', 'Breathing exercises']
    )

    if st.button('Save Preferences'):

        # Confirmation message
        st.write('Preferences saved!')

        # Display link only if the activity is Meditation
        if activity == 'Meditation':
            url = "https://www.cdc.gov/sleep/about/index.html"
            st.write("Check out this [meditation link](%s)" % url)
            st.video("https://www.youtube.com/watch?v=DbDoBzGY3vo")

        elif activity == 'Physical exercise':
            url = "https://health.gov/moveyourway#adults"
            st.write("Check out this [Pyhscial exercis link](%s)" % url)
            st.video("https://www.youtube.com/watch?v=fLLScgWQcHc")

        elif activity == 'Breathing exercises':
            url = "https://www.va.gov/vetsinworkplace/docs/em_eap_exercise_breathing.asp"
            st.write("Check out this [Breathing exercises link](%s)" % url)
            st.video("https://www.youtube.com/watch?v=FJJazKtH_9I")

    #save counts to file
    ad = pd.read_csv('pages\checkup.csv')
    account_read = ad.loc[(ad['account-name'] == st.session_state['name']) & (ad['account-username'] == st.session_state['username'])]

    account_read['happy-count'] = st.session_state.counters['happy']
    account_read['stress-count'] = st.session_state.counters['stress']
    account_read['anxiety-count'] = st.session_state.counters['anxiety']
    account_read['depressed-count'] = st.session_state.counters['depressed']

    ad.loc[(ad['account-name'] == st.session_state['name']) & (ad['account-username'] == st.session_state['username'])] = account_read

    # Write the DataFrame to the CSV file
    ad.to_csv('pages\checkup.csv')
    