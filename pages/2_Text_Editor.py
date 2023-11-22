import streamlit as st

from utils import init


init(st, 'Text Editor')
st.divider()

col1, col2 = st.columns(2, gap='medium')

content = col1.text_area('Content', "Start writing text from here...", height=250)

with col2:
    text, code, markdown = st.tabs(['Text', 'Code', 'Markdown'])
    text.text(content)
    code.code(content)
    markdown.markdown(content)

st.download_button('DOWNLOAD', content, file_name='data.txt', use_container_width=True)
