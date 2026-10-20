# Dashboard Visualisasi Data Interaktif Berbasis HCI dan UX

Dashboard lokal berbasis Python dan Streamlit untuk memantau performa penjualan dari dataset sintetis. Antarmukanya menerapkan prinsip **“Overview first, zoom and filter, details on demand”** agar ringkasan bisnis mudah dipahami sebelum pengguna menelusuri detail.

> Aplikasi dijalankan di komputer lokal melalui Visual Studio Code. Tidak memerlukan Google Colab atau layanan cloud.

## Fitur

- **Ringkasan KPI:** total penjualan, total profit, jumlah transaksi, dan transaksi gagal.
- **Filter interaktif:** saring transaksi berdasarkan wilayah dan kategori produk.
- **Grafik interaktif:** tren penjualan harian dan total penjualan per kategori, dengan nilai yang dapat dilihat melalui hover.
- **Detail saat dibutuhkan:** buka tabel transaksi mentah hanya jika diperlukan.
- **Dataset sintetis lokal:** 1.000 transaksi yang dihasilkan secara deterministik saat aplikasi dijalankan.

## Teknologi

- Python 3
- Streamlit
- Pandas
- NumPy
- Plotly Express

## Menjalankan secara lokal

1. Buka folder proyek ini di Visual Studio Code.
2. Buka terminal pada folder proyek.
3. Buat dan aktifkan virtual environment (disarankan):

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

4. Pasang dependensi:

   ```powershell
   python -m pip install -r requirements.txt
   ```

5. Jalankan dashboard:

   ```powershell
   python -m streamlit run app.py
   ```

6. Buka alamat lokal yang muncul di terminal, biasanya <http://localhost:8501>.

## Dataset

Dataset dibuat otomatis oleh aplikasi dan berisi 1.000 transaksi dengan atribut:

| Atribut | Deskripsi |
|---|---|
| Tanggal | Tanggal transaksi dalam rentang 180 hari mulai 1 Januari 2026 |
| Wilayah | Jakarta, Bengkulu, Bandung, atau Surabaya |
| Kategori | Elektronik, Pakaian, Makanan & Minuman, atau Buku |
| Penjualan | Nilai total transaksi dalam rupiah (IDR) |
| Profit | Nilai profit sintetis dalam rupiah (IDR) |
| Status | Selesai, Pending, atau Gagal |

Data dibuat dan diproses di komputer lokal. Aplikasi tidak membutuhkan dataset eksternal.

## Prinsip HCI dan UX

- **Overview first:** tempatkan KPI utama di bagian atas agar gambaran performa cepat ditangkap.
- **Zoom and filter:** sediakan filter wilayah dan kategori pada sidebar.
- **Details on demand:** tampilkan tabel transaksi hanya saat diminta.
- **Mengurangi extraneous load:** gunakan tata letak ringkas dan hindari dekorasi visual yang tidak mendukung pemahaman data.
- **Preattentive attributes:** gunakan warna dan posisi visualisasi untuk membantu pengguna membedakan informasi.

## Struktur proyek

```text
.
├── app.py
├── dokumentasi_proyek.txt
├── README.md
└── requirements.txt
```

## Referensi

Febriandirza, A. (2026). *Human Computer Interaction and Data Visualization*. Informatics Practitioner Lecture Series, Program Studi Informatika, Universitas Bengkulu.
