import streamlit as st
st.set_page_config(page_title="Docker", page_icon="📖",initial_sidebar_state="collapsed")
with open('header.html', 'r') as file:
        html_content = file.read()
        st.markdown(html_content, unsafe_allow_html=True)
st.title("Docker Course")

choice = st.select_slider("Choose content type:", ["Text", "Video"])

if choice == "Text":
    chapter = st.selectbox("Select a chapter:", ["Chapter 1", "Chapter 2", "Chapter 3", "Chapter 4"])

    if chapter == "Chapter 1":
        with open('docker1.html', 'r') as file:
            files = file.read()
            st.markdown(files, unsafe_allow_html=True)
    elif chapter == "Chapter 2":
                with open('docker2.html', 'r') as file:
                    files = file.read()
                    st.markdown(files, unsafe_allow_html=True)
    elif chapter == "Chapter 3":
        with open('docker3.html', 'r') as file:
            files = file.read()
            st.markdown(files, unsafe_allow_html=True)
    elif chapter == "Chapter 4":
        with open('docker4.html', 'r') as file:
            files = file.read()
            st.markdown(files, unsafe_allow_html=True)

else:

    st.markdown("""
                <br><br>
    <div style="text-align: center;">
<iframe width="800" height="500" src="https://www.youtube.com/embed/3c-iBn73dDE?si=oPMy4Z12M_mixPIK" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>    </div>
    """, unsafe_allow_html=True)