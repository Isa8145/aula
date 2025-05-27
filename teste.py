import streamlit as st
import pandas as pd

st.write("Olá! Qual é o seu nome?")

nome = st.text_input("Digite seu nome:")

if nome:
    st.write(f"Prazer em te conhecer, {nome}!")
    
    idade = st.number_input("Quantos anos você tem?", min_value=0, max_value=120, step=1)
    
    if idade:
        st.write(f"{nome}, daqui a 10 anos você terá {idade + 10} anos!")
