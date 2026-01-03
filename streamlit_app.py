import streamlit as st

st.title("Welcom to ADA APA DI LAB",text_alignment="center")
st.title(":green[Ada yang bisa di bantu?]",text_alignment="center")

from datetime import datetime

st.title("Aplikasi Hitung Usia")

# input data
nama = st.text_input("Masukkan nama")
tahun = st.number_input(
    "Masukkan tahun lahir",
    min_value=1900,
    max_value=datetime.now().year,
    step=1
)
kota = st.text_input("Masukkan asal kota")

# tombol aksi
if st.button("Hitung Usia"):
    usia = datetime.now().year - tahun
    st.success(
        f"Halo {nama}, usia Anda sekarang adalah {usia} tahun dan Anda tinggal di kota {kota}."
    )
