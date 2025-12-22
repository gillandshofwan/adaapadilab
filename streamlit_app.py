import streamlit as st

st.title("Welcom to ADA APA DI LAB",text_alignment="center")
st.title(":green[Ada yang bisa di bantu?]",text_alignment="center")

nama=input("masukan nama=")
tahun=int(input("masukan tahun lahir="))
kota=input("masukan asal kota=")

#menghitung usia
usia=2025-tahun

#kalimat
print ('halo',nama,'usia anda sekarang adalah',usia,'anda tinggal di kota',kota,)
