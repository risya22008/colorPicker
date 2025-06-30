# 🎨 Color Picker Generator

Aplikasi web interaktif berbasis Streamlit yang dapat mengekstrak 8 warna paling dominan dari gambar apa pun yang diunggah. Aplikasi ini menggunakan **K-Means Clustering** untuk mengidentifikasi palet warna secara otomatis. Sangat berguna bagi desainer, developer, atau siapa pun yang ingin mendapatkan skema warna yang konsisten dari sebuah gambar.

---

### ✨ [**Live Demo**](https://colorpicker-risya.streamlit.app/) ✨

---

## 🚀 Fitur Utama

-   ✅ **Upload Gambar**: Mendukung berbagai format gambar, termasuk `.jpg`, `.jpeg`, `.png`.
-   ✅ **Ekstraksi Warna Otomatis**: Secara cerdas mendeteksi dan menampilkan 8 warna paling dominan.
-   ✅ **Format Warna Lengkap**: Menampilkan warna dalam format **HEX** dan **RGB** untuk kemudahan penggunaan.
-   ✅ **UI Modern & Responsif**: Antarmuka yang bersih dengan pratinjau *real-time*.
-   ✅ **Interaktif**: Mudah digunakan bahkan untuk pemula sekalipun.

---

## 🖼️ Tampilan Aplikasi
![image](https://github.com/user-attachments/assets/f1b0b89d-39c3-49da-b89e-c5a921da4c52)


---

## 🧠 Cara Kerja

1.  **Upload Gambar**: Pengguna mengunggah file gambar melalui antarmuka Streamlit.
2.  **Pemrosesan**: Gambar diproses menggunakan OpenCV dan warnanya dikonversi ke format RGB.
3.  **Reshaping**: Piksel gambar diubah menjadi sebuah array datar untuk dianalisis.
4.  **Clustering**: Algoritma **K-Means** diterapkan untuk menemukan 8 *cluster* (pusat warna) yang paling dominan.
5.  **Konversi Warna**: Setiap pusat *cluster* dikonversi menjadi nilai HEX dan RGB.
6.  **Tampilan**: Palet warna yang dihasilkan ditampilkan secara dinamis di aplikasi.

---

## 📂 Struktur Proyek

```
.
├── app.py                 # File utama aplikasi Streamlit
├── requirements.txt       # Daftar dependensi Python
├── README.md              # Dokumentasi ini
└── example_input.jpg      # Contoh gambar (opsional)
```

---

## ⚙️ Dependensi

-   `streamlit`
-   `numpy`
-   `opencv-python`
-   `scikit-learn`
-   `matplotlib`

Semua dependensi dapat diinstal dengan mudah menggunakan file `requirements.txt` yang telah disediakan.

---

## 📌 Catatan

-   Proses K-Means mungkin memerlukan beberapa detik, tergantung pada ukuran dan kompleksitas gambar.
-   Aplikasi secara otomatis menangani konversi ruang warna (misalnya dari BGR ke RGB).
-   Hasil terbaik didapatkan dari gambar yang memiliki warna jelas dan cerah.
