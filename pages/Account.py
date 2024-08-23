import streamlit as st
import streamlit_authenticator as stauth
from authentication import authenticate_user, register_new_user

# Set the page configuration (must be the first Streamlit command)
st.set_page_config(layout='wide')

# Authenticate user
authenticate_user()

# Handle authentication status
if st.session_state.get('authentication_status'):
    st.write(f'Welcome *{st.session_state["name"]}*')
    st.title('Some content')
    # Password reset functionality
    if st.button("Reset Password"):
        new_password = st.text_input("New Password", type="password")
        if new_password:
            register_new_user.update_password(st.session_state['username'], new_password)

    # Update user details
    if st.button("Update Details"):
        new_email = st.text_input("New Email")
        if new_email:
            register_new_user.update_email(st.session_state['username'], new_email)

else:
    st.warning('Please log in to access this content.')
    st.subheader("Don't have an account? Register here!")
    register_new_user()
