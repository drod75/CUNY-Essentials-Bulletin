import streamlit as st

#access text file step 1: account checking
if not(st.session_state.get('authentication_status')):
    st.warning('Please Login to use this feature')
else:
    st.text('WIP')