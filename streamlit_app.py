import streamlit as st

st.title("Welcom to ADA APA DI LAB",text_alignment="center")
st.title(":green[Ada yang bisa di bantu?]",text_alignment="center")

nama= st.input("masukan nama=")
tahun= st.int(input("masukan tahun lahir="))
kota= st.input("masukan asal kota=")

#menghitung usia
usia=2025-tahun

#kalimat
st.write ('halo',nama,'usia anda sekarang adalah',usia,'anda tinggal di kota',kota,)
