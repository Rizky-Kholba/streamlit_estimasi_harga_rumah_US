import pickle
import streamlit as st

model = pickle.load(open('estimasi_rumah.sav', 'rb'))

st.title('Estimasi Harga Rumah Di US')

sqft_lot = st.number_input('Input Luas Tanah')
sqft_living = st.number_input('Input Luas Hunian')
bedrooms = st.number_input('Input Jumlah Kamar')
bathrooms = st.number_input('Input Jumlah Kamar Mandi')
floors = st.number_input('Input Lantai')

predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict(
        [[sqft_lot, sqft_living, bedrooms, bathrooms, floors]]
    )
    st.write ('Estimasi harga rumah bekas dalam USD : ', predict)
    st.write ('Estimasi harga rumah bekas dalam IDR (Juta) :', predict*15000)