import streamlit as st
import pickle
import string
from heapq import nlargest
import time
import nltk

normalized_frequencies = pickle.load(open("normalized_frequencies.pkl", "rb"))
stopwords = pickle.load(open("stopwords.pkl", "rb"))


# --------------------------- Functions -----------------------
def score_calculation(arr):
    dicts = {}
    for i in arr:
        score = 0
        holder = []
        text = i.lower()
        text = text.strip().split(" ")
        for b in text:
            if b not in stopwords and b not in string.punctuation:
                a = "".join([j for j in b if j not in string.punctuation])
                holder.append(a)

        for j in holder:
            if j in normalized_frequencies:
                score += normalized_frequencies[j]

        dicts[i] = score
    return dicts


def summary_generator(text):
    text = text.strip().split(".")
    d = score_calculation(text)
    l = int(len(d) * 0.3)
    res = nlargest(l, d, key=d.get)
    return ". ".join(res)


# --------------------------- UI --------------------------------
st.title("SUMMARY GENERATOR")

texted = st.text_area("Enter the para")

button = st.button("Summarize")

if button:
    summary = summary_generator(texted)
    with st.spinner('Wait for it...'):
        time.sleep(1)
    st.success('Done!')
    st.write(summary)
