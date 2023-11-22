import os
import json

import streamlit as st

from utils import init


def play(title: str, path: str):
    player_col.write(f'### Playing {title}')
    player_col.audio(os.path.join('musics', path))


init(st, 'Music Player')

player_col = st.columns(1)[0]

st.divider()

records = json.load(open('musics/records.json'))

for record in records:
    col1, col2, col3 = st.columns([.16, 1, .18])

    col1.image(f"musics/{record['image']}", use_column_width=True, width=20)

    with col2:
        st.write(f"### {record['title']}")
        st.write(f"**{record['artist']}**")

    with col3:
        if st.button('Play', use_container_width=True, key=record['title']):
            play(record['title'], record['source'])
        with st.expander('Credits'):
            st.markdown(record['credits'])
