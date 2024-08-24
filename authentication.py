import os
import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd

def authenticate_user():
    # Get the directory of the current script
    script_dir = os.path.dirname(__file__)

    # Construct the relative path to the config.yaml file
    config_path = os.path.join(script_dir, 'pages', 'config.yaml')

    # Load configuration file
    with open(config_path) as file:
        config = yaml.load(file, Loader=SafeLoader)

    # Initialize the authenticator
    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        config['pre-authorized']
    )

    # Perform user login with the correct arguments
    name, authentication_status, username = authenticator.login('main',max_concurrent_users=100)

    # Handle session state
    if authentication_status:
        st.session_state['name'] = name
        st.session_state['username'] = username
        st.session_state['authentication_status'] = True
    elif authentication_status == False:
        st.error('Username/password is incorrect')
    elif authentication_status == None:
        st.warning('Please enter your username and password')

    return authenticator, config, config_path

def register_user(config, config_path):
    # Collect user details
    st.write("Register New User")
    email = st.text_input("Email",key=100)
    username = st.text_input("Username",key=101)
    name = st.text_input("Name",key=102)
    password = st.text_input("Password", type="password",key=103)

    if st.button("Register",key=104):
        # Hash the password
        hashed_password = stauth.Hasher([password]).generate()[0]

        # Add new user to the credentials
        config['credentials']['usernames'][username] = {
            'name': name,
            'email': email,
            'password': hashed_password
        }

        # Save the updated configuration
        with open(config_path, 'w') as file:
            yaml.dump(config, file, default_flow_style=False)
    #add preliminary  values

        #add checkup row
        ad = pd.read_csv('checkup.csv')
        account_df = pd.DataFrame(data=[[name,username,0,0,0,0]], columns=['account-name','account-username','happy-count','stress-count','anxiety-count','depressed-count'])
        ad = pd.concat([ad,account_df],ignore_index=True)
        ad.to_csv('checkup.csv',index=False)

        #add journal row
        journal_data = pd.read_csv('journal_data.csv')
        jd_account = pd.DataFrame(data=[[name,username,"Welcome!\n"]], columns=['name','username','journal_string'])
        journal_data = pd.concat([journal_data,jd_account],ignore_index=True)
        journal_data.to_csv('journal_data.csv',index=False)
        
        st.success("User registered successfully! You can now log in.")

        



# Main execution block
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