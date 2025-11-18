
# Proyek Analisis Data: Dashboard Kualitas Udara Aotizhongxin

Sebuah dasboard interaktif untuk menganalisis data kualitas udara dari stasiun Aotizhongxin (2013-2017).

## Demo / Preview

https://github.com/user-attachments/assets/8769a345-62fd-4d31-ad8f-f670e2075366

## Daftar Isi

- [1. Identifikasi Proyek](#1-identifikasi-proyek)
- [2. Gambaran Arsitektur](#2-gambaran-arsitektur)
- [3. Instalasi & Pengaturan](#3-instalasi--pengaturan)

---

## 1. Identifikasi Proyek

### Pengantar / Tentang Proyek

Proyek ini menyediakan analisis data eksploratif (EDA) dan dashboard interaktif untuk dataset kualitas udara dari stasiun Aotizhongxin, Beijing, selama periode 1 Maret 2013 hingga 28 Februari 2017.

Tujuan utama proyek ini adalah untuk memvisualisasikan data dan menjawab pertanyaan bisnis spesifik mengenai polusi udara di area tersebut.

Proyek ini memecahkan masalah dalam memahami:

1. Bagaimana tren konsentrasi polutan partikulat (PM2.5 dan PM10) selama beberapa tahun terakhir?
2. Polutan gas mana (SO2, NO2, CO, O3) yang memiliki kontribusi rata-rata tertinggi terhadap polusi udara?

### Fitur Utama

- **Dashboard Interaktif:** Dibangun menggunakan Streamlit untuk eksplorasi data yang dinamis.
- **Filter Data:** Filter data berdasarkan tahun menggunakan widget *multiselect* di sidebar.
- **Visualisasi Tren:** Menampilkan plot tren tahunan untuk PM2.5/PM10 dan tren bulanan untuk polutan yang dipilih.
- **Perbandingan Polutan:** Diagram batang yang membandingkan konsentrasi rata-rata berbagai polutan gas (SO2, NO2, CO, O3).
- **Analisis Korelasi:** Scatter plot untuk menganalisis hubungan antara polutan (misalnya, PM2.5) dan faktor cuaca (misalnya, TEMP, WSPM).
- **Wawasan Langsung:** Kesimpulan analisis disajikan langsung di dashboard untuk interpretasi yang mudah.

---

## 2. Gambaran Arsitektur

### Tinjauan Tingkat Tinggi

Arsitektur proyek ini adalah aplikasi dashboard monolitik yang ditenagai oleh **Streamlit**. Aplikasi ini membaca data mentah dari file CSV, melakukan pemrosesan data dasar (filtering) menggunakan Pandas, dan menyajikan visualisasi menggunakan Matplotlib dan Seaborn. Data dimuat ke dalam cache (`@st.cache_data`) untuk mengoptimalkan performa saat interaksi.

### Struktur Direktori

Struktur folder utama proyek diatur sebagai berikut:

```xml

.
├── .devcontainer/
│   └── devcontainer.json   \# Konfigurasi environment pengembangan
├── dashboard/
│   └── dashboard.py        \# Skrip aplikasi utama Streamlit
├── data/
│   └── PRSA\_Data\_...csv    \# Dataset kualitas udara mentah
├── notebook.ipynb          \# Notebook analisis data eksploratif (EDA)
└── requirements.txt        \# Daftar dependensi Python

````

### Diagram Alur Dependensi

Diagram berikut mengilustrasikan alur data dasar dalam aplikasi dashboard:

```mermaid
graph TD
    A["Pengguna"] --> B["Streamlit Dashboard (dashboard.py)"]
    B --> C{Filter Tahun?}
    C -- Ya --> E["Filter Data (Pandas)"]
    C -- Tidak --> D["Load Data (Pandas @st.cache_data)"]
    E --> D
    D --> F["(data/PRSA_Data_...csv)"]
    D --> G["Visualisasi (Matplotlib/Seaborn)"]
    G --> B
````

### Ringkasan API Endpoints

Bagian ini tidak berlaku (N/A) karena proyek ini adalah aplikasi Streamlit dan bukan layanan API berbasis web.

---

## 3. Instalasi & Pengaturan

Proyek ini dirancang untuk dijalankan dengan mudah baik secara lokal maupun menggunakan VS Code Dev Containers.

### Prasyarat

  *-* Python (direkomendasikan 3.11, seperti yang ditentukan dalam `devcontainer.json`)
  *-* `pip` (Python package manager)
  *-* Dependensi yang tercantum dalam `requirements.txt`:
      *-* pandas
      *-* numpy
      *-* matplotlib
      *-* seaborn
      *-* streamlit
      *-* babel

### Langkah Instalasi

1. Clone repositori ini dari GitLab:

    ```bash
    git clone [https://gitlab.com/organization/repo.git](https://gitlab.com/organization/repo.git)
    cd repo
    ```

2. Buat dan aktifkan *virtual environment* (direkomendasikan):

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    # atau .\\venv\\Scripts\\activate di Windows
    ```

3. Instal dependensi yang diperlukan:

    ```bash
    pip install -r requirements.txt
    ```

### Konfigurasi

Tidak ada file `.env` atau konfigurasi variabel lingkungan yang diperlukan. Path dataset di-hardcode di dalam skrip untuk merujuk ke direktori `data/`.

### Instruksi Build

Tidak ada langkah *build* yang diperlukan untuk aplikasi berbasis skrip Python ini.

### Instruksi Menjalankan (Start)

1. Pastikan *virtual environment* Anda aktif.

2. Jalankan aplikasi Streamlit menggunakan perintah berikut:

    ```bash
    streamlit run dashboard/dashboard.py
    ```

3. Buka browser Anda dan akses `http://localhost:8501`.
