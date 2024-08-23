import streamlit as st
import streamlit_authenticator as stauth
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# MongoDB connection setup
def init_mongo_client():
    uri = "mongodb+srv://estebanmesa57:Brooklynishome1@cluster0.exl6d.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    client = MongoClient(uri, server_api=ServerApi('1'),document_class=dict)
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return client
    except Exception as e:
        print(f"An error occurred during MongoDB connection: {e}")
        return None

client = init_mongo_client()
if client:
    db = client["CUNYbulletin"]  # Rname of the DB
    users_collection = db['users']
else:
    st.error("Failed to connect to the database. Please check your credentials.")

# User authentication
def authenticate_user():
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")    

    if st.button("Login"):
        user = users_collection.find_one({"username": username})
        hashed_passwords = (stauth.Hasher([password]))
        if user and hashed_passwords.check_pw(password, user['password']):
            st.session_state['name'] = user['name']
            st.session_state['username'] = username
            st.session_state['authentication_status'] = True
        else:
            st.error('Username/password is incorrect')

# User registration
def register_new_user():
    st.write("Register New User")
    email = st.text_input("Email",key=0)
    username = st.text_input("Username",key=1)
    name = st.text_input("Name",key=2)
    password = st.text_input("Password", type="password",key=3)

    if st.button("Register"):
        hashed_password = stauth.Hasher([password]).generate()[0]
        user = {"name": name, "username": username, "email": email, "password": hashed_password}
        users_collection.insert_one(user)
        users_emotions_scores = db['users-emotions-scores']
        user_emotions = {
            'name':name,
            'username':username,
            'happy-count':0,
            'stress-count':0,
            'anxiety-count':0,
            'depressed-count':0
        }
        users_emotions_scores.insert_one(user_emotions)
        st.success("User registered successfully! You can now log in.")
        send_welcome_email(email, name)

# Password reset
def update_password(username, new_password):
    hashed_password = stauth.Hasher([new_password]).generate()[0]
    users_collection.update_one({"username": username}, {"$set": {"password": hashed_password}})
    st.success('Password modified successfully')

# Update email
def update_email(username, new_email):
    users_collection.update_one({"username": username}, {"$set": {"email": new_email}})
    st.success('Email updated successfully')

# Send welcome email
def send_welcome_email(to_email, student_name):
    subject = "Welcome to CUNY Essentials Bulletin"
    body = f"""
    Hey {student_name},

    Welcome to the CUNY Essentials Bulletin! We're pumped to have you with us. College can be tough, but we’re here to make sure you’ve got everything you need to succeed—both in class and in life.

    Get ready for updates on resources, and tips to keep you on track and feeling great. Remember, your mental health is our priority, so don’t hesitate to reach out if you need anything.

    Let’s make your time at CUNY awesome!

    Cheers,
    The CUNY Essentials Bulletin Team
    """

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
