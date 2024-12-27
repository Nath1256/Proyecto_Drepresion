import streamlit as st
import os
st.set_page_config(layout="wide")
st.title("Proyecto Final")
st.markdown(""" 
## 
El proyecto incluye las siguientes páginas:
""")
col1, col2=st.columns([2,2])
with col1:
    st.markdown('<div class=down>', unsafe_allow_html=true)
    #st.image("",width=250)
    st.markdown('</div>', unsafe_allow_html=true)
with col2:
    st.subheader("EDA: Analisis Exploratorio de datos")
    st.mardown("no se que poner acá")