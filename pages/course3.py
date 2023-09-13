import streamlit as st

st.set_page_config(page_title="Courses", page_icon="📚",layout="wide",initial_sidebar_state="collapsed")
with open('header.html', 'r') as file:
        header_html_content = file.read()
st.markdown(header_html_content, unsafe_allow_html=True)

with open('test3.html', 'r') as file:
        header_html_content = file.read()
st.markdown(header_html_content, unsafe_allow_html=True)


