import streamlit as st
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from textblob import TextBlob
import string
from sklearn.impute import KNNImputer
import numpy as np
import time
import os


st.set_page_config(page_title="Cleaner", page_icon="🧹",initial_sidebar_state="collapsed")
with open('header.html', 'r') as file:
        html_content = file.read()
        st.markdown(html_content, unsafe_allow_html=True)

def perform_data_cleaning(data):
     # Removing Trailing and Leading Whitespace
        data = data.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

        # Tokenization and lowercasing, Removing stop words, special characters, and punctuation
        nltk.download('punkt')
        nltk.download('stopwords')
        stop_words = set(stopwords.words('english'))

        def clean_text(data):
            if isinstance(data, str):
                tokens = word_tokenize(data)
                lowercase_tokens = [token.lower() for token in tokens]
                clean_tokens = [token for token in lowercase_tokens if token not in string.punctuation]
                filtered_tokens = [token for token in clean_tokens if token not in stop_words]
                return ' '.join(filtered_tokens)
            return data

        data = data.applymap(clean_text)

        # Stemming
        stemmer = PorterStemmer()

        def stem_text(data):
            if isinstance(data, str):
                stemmed_tokens = [stemmer.stem(token) for token in data.split()]
                return ' '.join(stemmed_tokens)
            return data

        data = data.applymap(stem_text)

        # Addressing Spelling and Format Errors

        def correct_spelling(text):
            if isinstance(text, str):
                blob = TextBlob(text)
                corrected_text = blob.correct()  
                return str(corrected_text)  
            return text

        for column in data.columns:
            if data[column].dtype == 'object':
                data[column] = data[column].apply(lambda x: correct_spelling(x))


        # Handling Missing Values
        data = data.fillna(data.mode().iloc[0])  

        # Data Imputation using K-Nearest Neighbors (KNN)
        numeric_columns = data.select_dtypes(include=[np.number]).columns
        if not numeric_columns.empty:
            knn_imputer = KNNImputer()
            data[numeric_columns] = pd.DataFrame(knn_imputer.fit_transform(data[numeric_columns]), columns=numeric_columns)

        # Removing Duplicates
        data = data.drop_duplicates()

        # Correcting Data Types
        data = data.infer_objects()

        # Removing Outliers
        zscore_threshold = 1
        numerical_columns = data.select_dtypes(include=[np.number]).columns
        z_scores = (data[numerical_columns] - data[numerical_columns].mean()) / data[numerical_columns].std()
        outliers_mask = np.abs(z_scores) > zscore_threshold
        data = data[~outliers_mask.any(axis=1)]

    
        return data


st.markdown("<div style='text-align:center;'><h1>Data Cleaning</h1></div>", unsafe_allow_html=True)
st.markdown("<div style='text-align:center;'>Upload CSV or XLSX File</div>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("", type=["csv", "xlsx"])

if uploaded_file is not None:
        file_extension = uploaded_file.name.split('.')[-1]

        # Load data from uploaded file
        if file_extension == 'csv':
            data = pd.read_csv(uploaded_file)
        elif file_extension == 'xlsx':
            data = pd.read_excel(uploaded_file)

        cleaned_data = perform_data_cleaning(data)

        progress_bar = st.progress(0)
        progress_text = st.empty()

        steps = [
                (10, "Removing Trailing and Leading Whitespace"),
                (20, "Tokenization and lowercasing"),
                (30, "Removing stop words"),
                (40, "Removing special characters, and punctuation."),
                (50, "Stemming or lemmatization"),
                (60, "Addressing Spelling and Format Errors"),
                (70, "Handling Missing Values"),
                (80, "Data Imputation"),
                (85, "Removing Duplicates"),
                (90, "Correcting data types"),
                (100, "Removing Outliers")
        ]
                

        for progress, text in steps:
            progress_bar.progress(progress)
            progress_text.text(text)
            time.sleep(3)

        progress_text.empty()
        progress_bar.empty()

        st.write("Original Data")
        st.dataframe(data)
        st.write("Cleaned Data")
        st.dataframe(cleaned_data)

        cleaned_data_filename = "cleaned_data" + os.path.splitext(uploaded_file.name)[1]
       
        if file_extension == 'csv':
            cleaned_data = cleaned_data.to_csv(index=False)
        elif file_extension == 'xlsx':
            cleaned_data = cleaned_data.to_excel(index=False)
        
        
        st.download_button(
            label="Download Cleaned Data",
            data=cleaned_data,
            file_name=cleaned_data_filename,
            key='download_button'
        )