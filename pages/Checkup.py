import streamlit as st

#access text file step 1: account checking
if not(st.session_state.get('authentication_status')):
    st.markdown('# Please Login to use this feature')
else:
    if 'counters' not in st.session_state:
        st.session_state.counters = {
            'happy': 0,
            'stress': 0,
            'anxiety': 0,
            'depressed': 0
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