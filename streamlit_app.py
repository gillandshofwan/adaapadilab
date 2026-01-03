import streamlit as st
from datetime import datetime

st.title("Aplikasi Hitung Usia")

# Input pengguna
nama = st.text_input("Masukkan nama")
tahun_lahir = st.number_input(
    "Masukkan tahun lahir",
    min_value=1900,
    max_value=datetime.now().year,
    step=1
)
kota = st.text_input("Masukkan asal kota")

# Proses & output
if st.button("Tampilkan Hasil"):
    usia = datetime.now().year - tahun_lahir
    st.write(
        f"Halo **{nama}**, usia Anda sekarang adalah **{usia} tahun**, "
        f"dan Anda tinggal di **{kota}**."
    )
