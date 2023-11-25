import streamlit as st
import smtplib
from email.mime.text import MIMEText

from utils import init


init(st, 'Mail App')


if st.session_state.get('email') is None:
    email = st.text_input('Your Email')
    password = st.text_input('App Password', type="password", help='get it from https://myaccount.google.com/apppasswords')

    if st.button('Login'):
        st.balloons()
        st.toast('Login!')
        st.session_state.update({'email': email})
        st.session_state.update({'password': password})
        st.rerun()

else:
    email_sender = st.session_state.get('email')
    password = st.session_state.get('password')
    st.write(f'Logged in as {email_sender}')
    email_receiver = st.text_input('Receiver\'s Email')
    subject = st.text_input('Subject')
    body = st.text_area('Body')

    if st.button("Send"):
        try:
            msg = MIMEText(body)
            msg['From'] = email_sender
            msg['To'] = email_receiver
            msg['Subject'] = subject

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(email_sender, password)
            server.sendmail(email_sender, email_receiver, msg.as_string())
            server.quit()

            st.toast('Email sent successfully!', icon='🚀')
        except Exception as e:
            st.error('Something went wrong! 😢')
            st.error(e)
