import streamlit as st
st.set_page_config(page_title="Python", page_icon="📖",initial_sidebar_state="collapsed")
with open('header.html', 'r') as file:
        html_content = file.read()
        st.markdown(html_content, unsafe_allow_html=True)
st.title("Python Course")

choice = st.select_slider("Choose content type:", ["Text", "Video"])

if choice == "Text":
    chapter = st.selectbox("Select a chapter:", ["Chapter 1", "Chapter 2", "Chapter 3", "Chapter 4", "Chapter 5","Chapter 6","Chapter 7","Chapter 8","Chapter 9","Chapter 10"])

    if chapter == "Chapter 1":
        with open('python1.html', 'r') as file:
            files = file.read()
            st.markdown(files, unsafe_allow_html=True)
    elif chapter == "Chapter 2":
                with open('python2.html', 'r') as file:
                    files = file.read()
                    st.markdown(files, unsafe_allow_html=True)
    elif chapter == "Chapter 3":
        with open('python3.html', 'r') as file:
            files = file.read()
            st.markdown(files, unsafe_allow_html=True)
    elif chapter == "Chapter 4":
        with open('python4.html', 'r') as file:
            files = file.read()
            st.markdown(files, unsafe_allow_html=True)
    elif chapter == "Chapter 5":
        with open('python5.html', 'r') as file:
            files = file.read()
            st.markdown(files, unsafe_allow_html=True)
    elif chapter == "Chapter 6":
        with open('python6.html', 'r') as file:
            files = file.read()
            st.markdown(files, unsafe_allow_html=True)
    elif chapter == "Chapter 7":
        with open('python7.html', 'r') as file:
            files = file.read()
            st.markdown(files, unsafe_allow_html=True)
    elif chapter == "Chapter 8":
        with open('python8.html', 'r') as file:
            files = file.read()
            st.markdown(files, unsafe_allow_html=True)
    elif chapter == "Chapter 9":
        with open('python9.html', 'r') as file:
            files = file.read()
            st.markdown(files, unsafe_allow_html=True)
    elif chapter == "Chapter 10":
        with open('python10.html', 'r') as file:
            files = file.read()
            st.markdown(files, unsafe_allow_html=True)
else:

    st.markdown("""
                <br><br><br>
    <div style="text-align: center;">
        <iframe width="800" height="500" src="https://www.youtube-nocookie.com/embed/gfDE2a7MKjA?si=Zu-k921cl01Zm2KQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
    </div>
    """, unsafe_allow_html=True)