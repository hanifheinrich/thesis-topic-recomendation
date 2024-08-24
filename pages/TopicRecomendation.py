import streamlit as st
import pandas as pd
import webbrowser as wb
from sklearn.naive_bayes import GaussianNB
from PIL import Image

st.header('Referensi Judul Tugas Akhir Sebelumnya')

dataea=pd.read_csv('dataset/ea.csv')
databi=pd.read_csv('dataset/bi.csv')
dataerp=pd.read_csv('dataset/erp.csv')
datasig=pd.read_csv('dataset/sig.csv')


st.subheader('Business Intelligence')
databi
st.subheader('Sistem Informasi Geografis')
datasig
st.subheader('Enterprise Architecture')
dataea
st.subheader('Enterprise Resource Planning')
dataerp

#referensi
url = 'http://scholar.unand.ac.id/'
st.subheader('Referensi terkait Rekomedasi Tugas Akhir lainnya dapat dilihat di')

if st.button('Klik Disini'):
    wb.open_new_tab(url)
    
