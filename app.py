import streamlit as st
import pickle
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import string 
ps= PorterStemmer()

nltk.download("stopwords")

ps=PorterStemmer()

def transform_text(text):
    text=text.lower()
    text=nltk.word_tokenize(text)
    y=[]
    for i in text:
        if i.isalnum():
            y.append(i)

    text=y[:]
    y.clear()
    for i in text:
        if i not in stopwords.words("english") and i not in string.punctuation:
            y.append(i)

    text=y[:]
    y.clear()
    for i in text:
        y.append(ps.stem(i))
    return " ".join(y)

tfidf=pickle.load(open("vectorizer.pkl","rb"))
model=pickle.load(open("model.pkl","rb"))

st.title("Spam classifier")

input_sms = st.text_area("Yahan apna message type karein:", placeholder="Example: You won a free lottery of $1000...")

# 3. Jab button click ho, tab kya karna hai?
if st.button('Predict'):
    
    # Step A: Text ko clean karna
    transformed_sms = transform_text(input_sms)
    
    # Step B: Text ko numbers (vectors) mein badalna
    vector_input = tfidf.transform([transformed_sms])
    
    # Step C: Model se prediction karwana
    result = model.predict(vector_input)[0]
    
    # Step D: Result screen par dikhana
    if result == 1:
        st.header("Spam 🚨")
    else:
        st.header("Not Spam ✅")