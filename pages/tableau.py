import streamlit as st
import pandas as pd
import pygwalker as pyg

st.set_page_config(page_title="Web-based Tableau", page_icon=":snake:", layout="wide",initial_sidebar_state="collapsed")

with open('header.html', 'r') as file:
        header_html_content = file.read()
st.markdown(header_html_content, unsafe_allow_html=True)

st.markdown("<div style='text-align:center;'><h1>Web-based Tableau</h1></div>", unsafe_allow_html=True)
st.markdown("<div style='text-align:center;'>Upload CSV or XLSX File</div>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("", type="csv")
if uploaded_file is not None:

        df = pd.read_csv(uploaded_file)
        st.subheader("Uploaded Data")
        st.write(df)

        st.title('Tableau')
        st.subheader('A demonstration of the Web-based Tableau')


        pyg.walk(df, env='Streamlit', dark='dark')