import streamlit as st

def footer():
    st.markdown(
        """
        <hr style="border-top: 1px solid #ccc; margin-bottom: 0;">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin: 0; padding: 20px 0;">
            <div style="margin: 0; padding: 0;">
                <h4>Contact Information</h4>
                <p><strong>1234 Data Street</strong></p>
                <p>Mumbai, India 400001</p>
                <p>Email: <a href="mailto:contact@datasensei.com">contact@datasensei.com</a></p>
                <p>Phone: <a href="tel:+919234567890">+91 923 456-7890</a></p>
            </div>
            <div style="margin: 0; padding: 0;">
                <h4>Quick Links</h4>
                <ul>
                    <li><a href="app" target="_self">Home</a></li>
                    <li><a href="tableau" target="_self">Tableau</a></li>
                    <li><a href="chat" target="_self">Chatbot</a></li>
                    <li><a href="contact" target="_self">Contact</a></li>
                </ul>
            </div>
            <div style="margin: 0; padding: 0;">
                <h4>Contact Us</h4>
                <form action="https://formsubmit.co/jain.rishabhkumar32754@gmail.com" method="POST">
                    <input type="hidden" name="_captcha" value="false">
                    <input type="text" name="name" placeholder="Your name" required>
                    <input type="email" name="email" placeholder="Your email" required>
                    <textarea name="message" placeholder="Your message here" rows="4" required></textarea>
                    <button type="submit" style="background-color: #007bff; color: #fff; border: none; padding: 10px 20px; cursor: pointer;">Send</button>
                </form>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

if __name__ == "__main__":
    footer()

