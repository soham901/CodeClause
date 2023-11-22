from difflib import SequenceMatcher

import streamlit as st

from utils import init


def check(s1: str, s2: str) -> int:
    if not s1 or not s2:
        return 0
    matcher = SequenceMatcher(None, s1.lower(), s2.lower())
    per = matcher.ratio() * 100
    return int(per)


init(st, 'Plagiarism Checker')
st.divider()

col1, col2 = st.columns(2)

p1 = col1.text_area('First Paragraph')
p2 = col2.text_area('Second Paragraph')

st.divider()

val = check(p1, p2)

st.progress(val, f'Matched {val}%')
