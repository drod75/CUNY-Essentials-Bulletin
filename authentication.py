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
    name, authentication_status, username = authenticator.login(location='main')

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
    email = st.text_input("Email")
    username = st.text_input("Username")
    name = st.text_input("Name")
    password = st.text_input("Password", type="password")

    if st.button("Register"):
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

        st.success("User registered successfully! You can now log in.")

        # Send a welcome email
        subject = "Welcome to CUNY Essentials Bulletin"
        body = get_welcome_email_body(name)
        send_email(email, subject, body)

        #add preliminary checkup values
        ad = pd.read_csv('pages\checkup_data\checkup.csv')
        account_df = pd.DataFrame({'account-name':name,
                                   'account-username':username,
                                   'happy-count':0,
                                   'stress-count':0,
                                   'anxiety-count':0,
                                   'depressed-count':0,
                                    })
        ad = ad.concat(account_df)

        # Write the DataFrame to the CSV file
        ad.to_csv('pages\checkup.csv')
    def send_email(to_email, subject, body):
        sender_email = "estebanmesa29@gmail.com"
        sender_password = "nonw doia uace ucra"

        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = to_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, message.as_string())
        server.quit()
        st.success(f"Welcome email sent to {to_email}")
    except Exception as e:
        st.error(f"Failed to send email: {e}")

def get_welcome_email_body(student_name):
    return f"""
    Hey {student_name},

    Welcome to the CUNY Essentials Bulletin! We're pumped to have you with us. College can be tough, but we’re here to make sure you’ve got everything you need to succeed—both in class and in life.

    Get ready for updates on resources, and tips to keep you on track and feeling great. Remember, your mental health is our priority, so don’t hesitate to reach out if you need anything.

    Let’s make your time at CUNY awesome!

    Cheers,
    The CUNY Essentials Bulletin Team
    """

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
