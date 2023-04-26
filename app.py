import streamlit as st
import pickle


normalized_frequencies=pickle.load(open("normalized_frequencies.pkl", "rb"))
st.title("SUMMARY GENERATOR")
