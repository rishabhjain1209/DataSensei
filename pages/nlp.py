import streamlit as st
st.set_page_config(page_title="NLP", page_icon="📖",initial_sidebar_state="collapsed")
with open('header.html', 'r') as file:
        html_content = file.read()
        st.markdown(html_content, unsafe_allow_html=True)
st.title("NLP Course")

choice = st.select_slider("Choose content type:", ["Text", "Video"])

if choice == "Text":
    chapter = st.selectbox("Select a chapter:", ["Chapter 1", "Chapter 2", "Chapter 3", "Chapter 4"])

    if chapter == "Chapter 1":
        with open('nlp1.html', 'r') as file:
            files = file.read()
            st.markdown(files, unsafe_allow_html=True)
    elif chapter == "Chapter 2":
                with open('nlp2.html', 'r') as file:
                    files = file.read()
                    st.markdown(files, unsafe_allow_html=True)
    elif chapter == "Chapter 3":
        with open('nlp3.html', 'r') as file:
            files = file.read()
            st.markdown(files, unsafe_allow_html=True)
    elif chapter == "Chapter 4":
        with open('nlp4.html', 'r') as file:
            files = file.read()
            st.markdown(files, unsafe_allow_html=True)
else:

    st.markdown("""
                <br><br><br>
    <div style="text-align: center;">
<iframe width="800" height="500" src="https://www.youtube.com/embed/68lIfswwG2A?si=wTy6rExgepr5KTTp" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>                  """, unsafe_allow_html=True)