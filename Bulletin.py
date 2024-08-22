import sys
import subprocess

with open(r'requirements.txt', r) as file:
    for line in file:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', line])

        reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
        installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

import streamlit as st
import streamlit_authenticator as stauth

def wide_space_default():
    st.set_page_config(layout='wide')
wide_space_default()

st.title('CUNY Essentials Bulletin')
st.text('Welcome to the CUNY Essentials Bulletin! \nHere you will find the resources needed to contact help and document your feelings!')
st.text('In this site there are two main pages:')
st.markdown('* __Journal__ where you can document how you feel')
st.markdown('* __Essentials__ where you can find the many mental health services CUNY and the government provides')
st.text('With this we hope you make full use of our site and get any help you need, \nthere are people always here for you!')
#just makeing sure this works
# i hope this works now....
