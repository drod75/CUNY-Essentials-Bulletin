import streamlit as st
import pandas as pd

#access text file step 1: account checking
if not(st.session_state.get('authentication_status')):
    st.markdown('# Please Login to use this feature')
else:
    if 'counters' not in st.session_state:
        #read checkup values, auto set to 0 for new accounts in authentication
        ad = pd.read_csv('checkup.csv')
        account_read = ad.loc[(ad['account-name'] == st.session_state['name']) & (ad['account-username'] == st.session_state['username'])]
        happy = account_read['happy-count']
        stress = account_read['stress-count']
        anxiety = account_read['anxiety-count']
        depressed = account_read['depressed-count']
        st.session_state.counters = {
            'happy': happy,
            'stress': stress,
            'anxiety': anxiety,
            'depressed': depressed
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
    ad = pd.read_csv('checkup.csv')
    ad.loc[(ad['account-name'] == st.session_state['name']) & (ad['account-username'] == st.session_state['username']), 'happy-count'] = int(st.session_state.counters['happy'])
    ad.loc[(ad['account-name'] == st.session_state['name']) & (ad['account-username'] == st.session_state['username']), 'stress-count'] = int(st.session_state.counters['stress'])
    ad.loc[(ad['account-name'] == st.session_state['name']) & (ad['account-username'] == st.session_state['username']), 'anxiety-count'] = int(st.session_state.counters['anxiety'])
    ad.loc[(ad['account-name'] == st.session_state['name']) & (ad['account-username'] == st.session_state['username']), 'depressed-count'] = int(st.session_state.counters['depressed'])

    ad = ad[['account-name','account-username','happy-count','stress-count','anxiety-count','depressed-count']]
    # Write the DataFrame to the CSV file
    ad.to_csv('checkup.csv',index=False)
    