import streamlit as st
import pandas as pd
from authentication import db

#access text file step 1: account checking
if not(st.session_state.get('authentication_status')):
    st.markdown('# Please Login to use this feature')
else:
    if 'counters' not in st.session_state:
        #db read values
        users_emotions_scores = db['users-emotion-scores']
        account_active = users_emotions_scores.find_one({"username": st.session_state['username']})
        st.session_state.counters['happy'] = account_active['happy-count']
        st.session_state.counters['stress'] = account_active['stress-count']
        st.session_state.counters['anxiety'] = account_active['anxiety-count']
        st.session_state.counters['depressed'] = account_active['depressed-count']

        st.session_state.counters = {
            'happy': st.session_state.counters['happy'],
            'stress': st.session_state.counters['stress'],
            'anxiety': st.session_state.counters['anxiety'],
            'depressed': st.session_state.counters['depressed']
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

    #db update
    users_emotions_scores.update_one({"username": st.session_state['username']}, {"$set": {"happy-count": st.session_state.counters['happy']}})
    users_emotions_scores.update_one({"username": st.session_state['username']}, {"$set": {"stress-count": st.session_state.counters['stress']}})
    users_emotions_scores.update_one({"username": st.session_state['username']}, {"$set": {"anxiety-count": st.session_state.counters['anxiety']}})
    users_emotions_scores.update_one({"username": st.session_state['username']}, {"$set": {"depressed-count": st.session_state.counters['depressed']}})

    