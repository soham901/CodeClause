import streamlit


def init(st: streamlit, title) -> None:
    st.set_page_config(
        page_title=title,
        page_icon=":fire:",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'About': '''
                ## I completed an Python Internship at *Code Clause*
                i created an music player, text editor, mail application and plagiarism checker
            '''
        }
    )

    st.title(title)

    hide_streamlit_style = '''
    <style>
    {visibility: hidden !important;}
    footer {visibility: hidden !important;}
    </style>
    '''

    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
