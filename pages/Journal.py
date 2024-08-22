import streamlit as st
from Bulletin import authentication_status

if authentication_status is False:
    st.warning('Please Login')
else:
    st.text('In Progress')