import streamlit as st

from utils import init

init(st, 'Soham | CodeClause Internship')

st.divider()

st.write('#### I completed an Python Internship at *Code Clause* on 23rd November 2023')
st.write("During this internship, I've used the following technologies:")
st.write("""
- Python3
- Streamlit
- SMTP
- Git
- GitHub
""")

with st.expander("Connect with me"):
    col1, col2, col3 = st.columns(3)
    col1.link_button("LinkedIn", "https://linkedin.com/in/soham-sagathiya", use_container_width=True)
    col2.link_button("Gmail", "mailto:sagathiyasoham12345@gmail.com", use_container_width=True)
    col3.link_button("GitHub", "https://github.com/soham901", use_container_width=True)
