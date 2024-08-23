import streamlit as st
from streamlit_ace import st_ace, KEYBINDINGS, LANGUAGES, THEMES
import pandas as pd

#access text file step 1: account checking
if not(st.session_state.get('authentication_status')):
    st.markdown('# Please Login to use this feature')
else:
    st.set_page_config(layout="wide")
    if 'journal' not in st.session_state:
         st.session_state.journal = ''

    user_input = st.text_area("Write your Journal below", height=500)

    if st.button("Save Journal"):
        if user_input:
            st.session_state.journal += f"{str(user_input)}\n\n"

            #load dataframe to write
            df = pd.read_csv('journal_data.csv')
            ap_check = df.loc[(df['name'] == st.session_state['name']) & (df['username'] == st.session_state['username'])]
            journal_saved = str(ap_check['journal_string'])
            journal_saved = journal_saved + str(st.session_state.journal)
            
            st.write("### Saved Journal:")
            st.write(st.session_state.journal)

            #save data
            df.loc[(df['name'] == st.session_state['name']) & (df['username'] == st.session_state['username']), 'journal_string'] = str(st.session_state.journal)
            df.to_csv('journal_data.csv', index=False)

            st.success("Journal saved successfully!")
        else:
            st.warning("You have not written anything to save.")
    # Show the saved journal content
    text = st.empty()
    
    
      