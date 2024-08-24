![image](https://github.com/user-attachments/assets/e449d0cc-a9c8-4e3d-8432-29b518b0f713)# Web Rekomendasi Topik Tugas Akhir Mahasiswa Departemen Sistem Informasi Unand

Tugas akhir merupakan tahap akhir dari program studi yang menuntut mahasiswa untuk mengaplikasikan pengetahuan yang mereka peroleh selama kuliah dalam suatu proyek. Namun, seringkali mahasiswa kesulitan dalam memilih topik yang sesuai dengan minat dan kemampuan mereka, terutama dalam lingkup yang luas seperti sistem informasi.

## Table of Contents:

- Dataset
- K-Means Clustering
- Naive Bayes Classification
- Streamlit Deployment
- Preview
  
## Dataset
Dataset yang digunakan kali ini adalah data dummy yang dibuat menggunakan fungsi excel.Jumlah dataset yang digunakan adalah sebanyak 150 row data.
Menggunakan Twitter API, saya mengumpulkan 999 tweet dengan kata kunci "Karen's Dinner" untuk analisis sentimen dan tren percakapan.
Score = `INDEX($O$4:$O$10,RANDBETWEEN(1,COUNTA[$O$4:$O$10)},1)`

## K-Means Clustering
Klaster yang dibentuk adalah empat yang merepresentasikan profil lulusan DSI Unand yang antara lain; ERP, EA, GIS, dan BI. Proses klasterisasi kali ini menggunakan algortima K-Means. Kluster ini nantinya akan digunakan sebagai atribut target dalam proses klasifikasi.
```python
scaler_fit = MinMaxScaler()
scaled_x = scaler_fit.fit_transform(array_x)
kmeans = KMeans(n_clusters = 4, random_state=123)
kmeans.fit(scaled_x)
print(kmeans.cluster_centers_)
dataset["kluster"] = kmeans.labels_
print(dataset.kluster)
```

## Naive Bayes Classification
Penerapan metode Naive Bayes pada dataset yang terdiri dari 150 data dengan pembagian data testing sebesar 20% dan data training sebesar 80% menghasilkan akurasi sebesar 83% berdasarkan confusion matrix.
```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf=GaussianNB()
clf.fit(X_train,y_train)
y_pred=clf.predict(X_test)
print(classification_report(y_test,y_pred))
```

## Streamlit Deployment
Pengimplementasian model dilakukan dengan cara menerapkan model yang telah dibuat sebelumnya ke dalam Streamlit. Streamlit adalah sebuah framework open-source yang digunakan untuk membangun antarmuka pengguna interaktif untuk aplikasi data dan machine learning
```python
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
```

## Preview
![image](https://github.com/user-attachments/assets/b39c8dc0-751d-4640-9a37-05c1fe17c7bd)
![image](https://github.com/user-attachments/assets/ad15a71b-0b05-490d-8239-ca3ed16485e4)

