import streamlit as st

st.title("Welcom to ADA APA DI LAB",text_alignment="center")
st.title(":green[Ada yang bisa di bantu?]",text_alignment="center")

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
