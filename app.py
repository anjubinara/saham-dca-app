import streamlit as st

st.title("Kalkulator Rata-rata Saham + DCA")
st.markdown("Masukkan pembelian awal dan DCA kamu, lalu lihat rata-rata harga & simulasi cuan!")

# Rekap pembelian
rekap = []

# Pembelian awal
st.header("Pembelian Awal")
harga_awal = st.number_input("Harga beli awal", min_value=1.0)
lot_awal = st.number_input("Jumlah lot awal", min_value=1, step=1)

if harga_awal and lot_awal:
    biaya_awal = harga_awal * lot_awal * 100
    rekap.append(("Pembelian awal", harga_awal, lot_awal, biaya_awal))

# DCA
st.header("Tambahkan DCA")
dca_list = []
dca_count = st.number_input("Berapa kali DCA?", min_value=0, step=1)

for i in range(dca_count):
    st.subheader(f"DCA ke-{i+1}")
    harga = st.number_input(f"Harga DCA ke-{i+1}", min_value=1.0, key=f"harga_dca_{i}")
    lot = st.number_input(f"Lot DCA ke-{i+1}", min_value=1, step=1, key=f"lot_dca_{i}")
    biaya = harga * lot * 100
    rekap.append((f"DCA ke-{i+1}", harga, lot, biaya))

# Proses dan hitung
if st.button("Hitung Rata-rata & Simulasi") and rekap:
    total_lot = sum(r[2] for r in rekap)
    total_biaya = sum(r[3] for r in rekap)
    rata_rata = total_biaya / (total_lot * 100)

    st.subheader("Rekap Pembelian")
    for r in rekap:
        st.write(f"{r[0]}: {r[2]} lot x {r[1]} = Rp{r[3]:,.0f}")

    st.subheader("Hasil Akhir")
    st.write(f"Total lot: {total_lot}")
    st.write(f"Total saham (lembar): {total_lot * 100}")
    st.write(f"Total biaya: Rp{total_biaya:,.0f}")
    st.write(f"Harga rata-rata: {rata_rata:.2f}")

    st.subheader("Target Cuan")
    for p in [2, 5, 7, 10, 12, 15, 20]:
        st.write(f"Cuan {p}% → {rata_rata * (1 + p/100):.2f}")

    # Simulasi jual
    st.subheader("Simulasi Penjualan")
    harga_jual = st.number_input("Masukkan harga jual", min_value=1.0, step=1.0)
    if harga_jual:
        total_jual = harga_jual * total_lot * 100
        selisih = total_jual - total_biaya
        persen = (selisih / total_biaya) * 100
        status = "Untung" if selisih > 0 else "Rugi" if selisih < 0 else "Impas"
        st.write(f"{status}! {'Untung' if selisih > 0 else 'Rugi'} Rp{abs(selisih):,.0f} ({persen:.2f}%)")
        st.write(f"Total nilai penjualan: Rp{total_jual:,.0f}")