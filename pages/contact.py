import streamlit as st

st.set_page_config(page_title="Contact", page_icon="📞",initial_sidebar_state="collapsed")

with open('header.html', 'r') as file:
        header_html_content = file.read()
st.markdown(header_html_content, unsafe_allow_html=True)

st.markdown("""
<style>
input[type=text], input[type=email], textarea {
    width: 100%; 
    padding: 12px; 
    border: 1px solid #ccc; 
    border-radius: 4px; 
    box-sizing: border-box;
    margin-top: 6px;
    margin-bottom: 16px; 
    resize: vertical
}
</style>
            """,unsafe_allow_html=True)

st.header(":mailbox: Get In Touch With Me!")


st.markdown( """
<div class="container">
<form action="https://formsubmit.co/jain.rishabhkumar32754@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
</div>
""", unsafe_allow_html=True)

