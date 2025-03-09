import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul Dashboard
st.title("Dashboard Kualitas Udara di Aotizhongxin")

# Load Dataset
@st.cache_data  # Cache data untuk mempercepat loading
def load_data():
    data = pd.read_csv("data/PRSA_Data_Aotizhongxin_20130301-20170228.csv")  # Ganti dengan nama file Anda
    return data

df = load_data()

# Sidebar untuk filter
st.sidebar.header("Filter Data")
year_filter = st.sidebar.multiselect(
    "Pilih Tahun",
    options=sorted(df["year"].unique()),
    default=sorted(df["year"].unique())
)
filtered_df = df[df["year"].isin(year_filter)] if year_filter else df

# 1. Tampilan Data
st.header("Tampilan Data")
st.write(filtered_df)

# 2. Statistik Deskriptif
st.header("Statistik Deskriptif")
st.write(filtered_df.describe())

# 3. Visualisasi Tren Polutan
st.header("Visualisasi Tren Polutan")
pollutants = ["PM2.5", "PM10", "CO", "NO2", "SO2", "O3"]
selected_pollutant = st.selectbox("Pilih Polutan", pollutants)

# Plot tren polutan
plt.figure(figsize=(10, 6))
sns.lineplot(data=filtered_df, x="month", y=selected_pollutant, ci=None)
plt.title(f"Tren {selected_pollutant} per Bulan")
plt.xlabel("Bulan")
plt.ylabel(selected_pollutant)
st.pyplot(plt)

# Agregasi data berdasarkan tahun
yearly_data = filtered_df.groupby('year')[['PM2.5', 'PM10']].mean().reset_index()

# Plot tren PM2.5 dan PM10
st.header("Tren Konsentrasi PM2.5 dan PM10")
plt.figure(figsize=(10, 6))
plt.plot(yearly_data['year'], yearly_data['PM2.5'], label='PM2.5', marker='o', color='blue')
plt.plot(yearly_data['year'], yearly_data['PM10'], label='PM10', marker='x', color='orange')
plt.xlabel('Tahun')
plt.ylabel('Konsentrasi Rata-Rata (µg/m³)')
plt.title('Tren Konsentrasi PM2.5 dan PM10 di Aotizhongxin')
plt.xticks(yearly_data['year'])
plt.legend()
plt.grid(True)
st.pyplot(plt)

# Insight tentang tren
st.subheader("Insight:")
st.write("""
- **PM2.5**: Menunjukkan tren fluktuasi dari tahun ke tahun. Peningkatan signifikan terjadi pada tahun-tahun tertentu, seperti 2017.
- **PM10**: Secara umum memiliki konsentrasi lebih tinggi dibandingkan PM2.5. Tren PM10 juga menunjukkan pola penurunan pada tahun-tahun tertentu, seperti 2016.
- Baik PM2.5 maupun PM10 menunjukkan lonjakan pada musim dingin, yang mungkin disebabkan oleh pembakaran bahan bakar untuk pemanasan.
""")

# Informasi tambahan
st.subheader("Informasi Tambahan:")
st.write("""
- Data mencakup periode dari Maret 2013 hingga Februari 2017.
- Konsentrasi PM2.5 dan PM10 dihitung sebagai rata-rata tahunan untuk mempermudah visualisasi tren jangka panjang.
""")

# 5. Hubungan Antar Variabel
st.header("Hubungan Antar Variabel")
x_var = st.selectbox("Pilih Variabel X", ["TEMP", "PRES", "DEWP", "RAIN", "WSPM"])
y_var = st.selectbox("Pilih Variabel Y", pollutants)

# Scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=filtered_df, x=x_var, y=y_var, alpha=0.5)
plt.title(f"Hubungan antara {x_var} dan {y_var}")
plt.xlabel(x_var)
plt.ylabel(y_var)
st.pyplot(plt)

# Daftar polutan
pollutants = ['SO2', 'NO2', 'CO', 'O3']

# Menghitung rata-rata konsentrasi polutan
average_pollutant_concentrations = df[pollutants].mean()

# Visualisasi menggunakan Matplotlib
st.header("Grafik Rata-Rata Konsentrasi Polutan")
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(pollutants, average_pollutant_concentrations, color=['blue', 'orange', 'green', 'red'])
ax.set_xlabel('Polutan')
ax.set_ylabel('Rata-Rata Konsentrasi (µg/m³)')
ax.set_title('Rata-Rata Konsentrasi Polutan di Aotizhongxin')
ax.set_ylim(0, max(average_pollutant_concentrations) * 1.2)  # Menambahkan margin pada sumbu y

# Menampilkan grafik di Streamlit
st.pyplot(fig)

# Insight tentang rata-rata konsentrasi polutan
st.subheader("Insight:")
st.write("""
- **CO**: Menunjukkan konsentrasi rata-rata tertinggi di antara semua polutan, mencapai sekitar 1200 µg/m³. Ini menunjukkan bahwa pembakaran bahan bakar fosil (misalnya, kendaraan bermotor dan pemanasan) adalah sumber utama polusi udara di Aotizhongxin.
- **O3**: Memiliki konsentrasi rata-rata sedang, sekitar 50 µg/m³, yang lebih tinggi dibandingkan SO2 dan NO2 tetapi jauh lebih rendah dari CO.
- **NO2**: Konsentrasi rata-rata NO2 relatif rendah, sekitar 50 µg/m³, namun tetap menjadi faktor penting dalam polusi udara.
- **SO2**: Konsentrasi rata-rata SO2 sangat rendah, mendekati 0 µg/m³, yang mengindikasikan kontribusi minimal terhadap polusi udara.
""")