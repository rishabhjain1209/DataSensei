import streamlit as st
st.set_page_config(page_title="Numpy", page_icon="📖",initial_sidebar_state="collapsed")
with open('header.html', 'r') as file:
        html_content = file.read()
        st.markdown(html_content, unsafe_allow_html=True)
st.title("Numpy Course")

choice = st.select_slider("Choose content type:", ["Text", "Video"])

if choice == "Text":
    chapter = st.selectbox("Select a chapter:", ["Chapter 1", "Chapter 2", "Chapter 3", "Chapter 4", "Chapter 5","Chapter 6","Chapter 7"])

    if chapter == "Chapter 1":
        with open('numpy1.html', 'r') as file:
            files = file.read()
            st.markdown(files, unsafe_allow_html=True)
    elif chapter == "Chapter 2":
                with open('numpy2.html', 'r') as file:
                    files = file.read()
                    st.markdown(files, unsafe_allow_html=True)
    elif chapter == "Chapter 3":
        with open('numpy3.html', 'r') as file:
            files = file.read()
            st.markdown(files, unsafe_allow_html=True)
    elif chapter == "Chapter 4":
        with open('numpy4.html', 'r') as file:
            files = file.read()
            st.markdown(files, unsafe_allow_html=True)
    elif chapter == "Chapter 5":
        with open('numpy5.html', 'r') as file:
            files = file.read()
            st.markdown(files, unsafe_allow_html=True)
    elif chapter == "Chapter 6":
        with open('numpy6.html', 'r') as file:
            files = file.read()
            st.markdown(files, unsafe_allow_html=True)
    elif chapter == "Chapter 7":
                with open('numpy7.html', 'r') as file:
                    files = file.read()
                    st.markdown(files, unsafe_allow_html=True)

else:

    st.markdown("""
                <br><br><br>
    <div style="text-align: center;">
<iframe width="800" height="500" src="https://www.youtube.com/embed/Rbh1rieb3zc?si=yO5V8Mkz5_g18S7D" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>    </div>
    """, unsafe_allow_html=True)