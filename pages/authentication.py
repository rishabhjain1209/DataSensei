import streamlit as st
import bcrypt
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

st.set_page_config(page_title="Authentication", page_icon="🔒", initial_sidebar_state="collapsed")


uri = "mongodb+srv://jainrishabhkumar32754:Mongo2503@cluster0.lxnvmsz.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

with open('header.html', 'r') as file:
        header_html_content = file.read()
st.markdown(header_html_content, unsafe_allow_html=True)

db = client["users"]
users_collection = db["users"]

def create_user(username, password):
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    user_data = {"username": username, "password": hashed_password}
    users_collection.insert_one(user_data)
    st.session_state['username'] = username

def verify_user(username, password):
    user_data = users_collection.find_one({"username": username})
    if user_data:
        st.session_state['username'] = username
        return bcrypt.checkpw(password.encode("utf-8"), user_data["password"])
    return False

st.title("Authentication 🔒")

choice = st.select_slider('',['Sign Up','Login'])

if choice == 'Login':
    username=st.text_input('Username')
    password=st.text_input('Password',type="password")
    if st.button("Login"):
            if verify_user(username, password):
                st.success("Login successful!")
                st.balloons()
            else:
                st.error("Invalid credentials")

else:
    name=st.text_input('Name')
    username=st.text_input('Username')
    password=st.text_input('Password',type="password")
    if st.button("Submit"):
            create_user(username, password)
            st.success("Sign-in successful! You can now log in.")
            st.balloons()


