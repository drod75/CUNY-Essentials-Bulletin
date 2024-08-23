import streamlit as st
from streamlit_ace import st_ace, KEYBINDINGS, LANGUAGES, THEMES
import pandas as pd

#access text file step 1: account checking
if not(st.session_state.get('authentication_status')):
    st.markdown('# Please Login to use this feature')
else:
    st.set_page_config(layout="wide")
    if 'journal' not in st.session_state:
        st.session_state.journal = ""
    journal_csv = pd.read_csv('journal_data.csv')
    account_active = journal_csv.loc[(journal_csv['name'] == st.session_state['name']) & (journal_csv['username'] == st.session_state['username'])]
    st.session_state.journal = account_active['journal_string']
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

    account_active = account_active[['name','username','journal_string']]
    journal_csv.update(account_active,overwrite=True)
    journal_csv = journal_csv[['name','username','journal_string']]    
    # Write the DataFrame to the CSV file
    journal_csv.to_csv('journal_data.csv',index=False)
      