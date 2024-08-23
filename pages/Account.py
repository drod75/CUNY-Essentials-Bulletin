import streamlit as st
from authentication import authenticate_user, register_user
import yaml

st.set_page_config(layout='wide')

# Authenticate user
authenticator, config, config_path = authenticate_user()

# Handle authentication status
if st.session_state.get('authentication_status'):
    authenticator.logout()
    st.write(f'Welcome *{st.session_state["name"]}*')
    st.title('Some content')

    # Password reset functionality
    try:
        if authenticator.reset_password(st.session_state['username']):
            st.success('Password modified successfully')
    except Exception as e:
        st.error(e)

    # User registration
    register_user(config, config_path)

    # Forgot password functionality
    try:
        username_of_forgotten_password, email_of_forgotten_password, new_random_password = authenticator.forgot_password()
        if username_of_forgotten_password:
            st.success('New password to be sent securely')
        elif username_of_forgotten_password is False:
            st.error('Username not found')
    except Exception as e:
        st.error(e)

    # Forgot username functionality
    try:
        username_of_forgotten_username, email_of_forgotten_username = authenticator.forgot_username()
        if username_of_forgotten_username:
            st.success('Username to be sent securely')
        elif username_of_forgotten_username is False:
            st.error('Email not found')
    except Exception as e:
        st.error(e)

    # Update user details
    try:
        if authenticator.update_user_details(st.session_state['username']):
            st.success('Entries updated successfully')
    except Exception as e:
        st.error(e)

    # Save the updated configuration
    with open(config_path, 'w') as file:
        yaml.dump(config, file, default_flow_style=False)
else:
    st.warning('Please log in to access this content.')
    
    # Add a "Register" section
    st.subheader("Don't have an account? Register here!")
    register_user(config, config_path)