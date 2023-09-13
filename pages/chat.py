import streamlit as st
import wikipedia
import speech_recognition as sr
from gtts import gTTS
import os
import pyttsx3


st.set_page_config(page_title="Chatbot", page_icon="🤖", initial_sidebar_state="collapsed")

with open('header.html', 'r') as file:
        header_html_content = file.read()
st.markdown(header_html_content, unsafe_allow_html=True)

st.markdown("<div style='text-align:center;'><h1>ChatBot </h1></div>", unsafe_allow_html=True)

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 250)
    engine.say(text)
    engine.runAndWait()


def search_wikipedia(query):
        try:
            sentences=5
            summary = wikipedia.summary(query, sentences=sentences)
            return summary
        except wikipedia.exceptions.DisambiguationError as e:
            return f"Disambiguation Error: {e.options}"
        except wikipedia.exceptions.PageError as e:
            return "Page not found."
        


choice = st.select_slider('',['Chat','Talk'])

if choice == 'Chat':
    user_input = st.text_input("You: ")
    chat_history = []
    if st.button("Submit"):
        summary=search_wikipedia(user_input)
        chat_history.append(f"You: {user_input}")
        chat_history.extend([f"Bot🤖:   {summary}" ])
        for message in chat_history:
                    st.write(message)
        if st.button("Clear Chat History"):
                chat_history = []


else:

    st.title("Virtual Assistant")

    st.write("Speak something...")
    user_input = st.button("Start Recording")

    if user_input:
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()

        with microphone as source:
            st.write("Listening...")
            audio = recognizer.listen(source)

        st.write("Recognizing...")

        try:
            user_query = recognizer.recognize_google(audio)
            st.write("You said:", user_query)
            response_summary = search_wikipedia(user_query)
            speak(response_summary)
        except sr.UnknownValueError:
            st.write("Sorry, I couldn't understand your audio.")
        except sr.RequestError as e:
            st.write("Sorry, there was an error. Please check your internet connection.")
    if os.path.exists("response.mp3"):
        os.remove("response.mp3")