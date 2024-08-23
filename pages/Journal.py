import streamlit as st
from streamlit_ace import st_ace, KEYBINDINGS, LANGUAGES, THEMES

#access text file step 1: account checking
if not(st.session_state.get('authentication_status')):
    st.markdown('# Please Login to use this feature')
else:
    st.set_page_config(layout="wide")
    if 'journal' not in st.session_state:
        st.session_state.journal = ""
    user_input = st.text_area("Write your Journal below", height=500)

    if st.button("Save Journal"):
        if user_input:
            st.session_state.journal += f"{user_input}\n\n" 
            st.success("Journal saved successfully!")
        else:
            st.warning("You have not written anything to save.")
    # Show the saved journal content
    st.write("### Saved Journal:")
    text = st.empty()
    st.write(st.session_state.journal)

