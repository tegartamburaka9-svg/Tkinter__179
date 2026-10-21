import tkinter as tk
from tkinter import messagebox

def hitung_prediksi():
    """
    Fungsi Hasil Prediksi yang akan menuliskan prodi 'Teknologi Informasi' 
    apapun nilai atau input yang diberikan oleh pengguna.
    """
    # Memeriksa apakah semua kotak input sudah diisi (validasi sederhana)
    for entry in entry_list:
        if not entry.get().strip():
            messagebox.showwarning("Peringatan", "Harap isi semua nilai mata pelajaran terlebih dahulu!")
            return

    # Mengatur teks pada label luaran hasil prediksi
    label_luaran.config(
        text="Hasil Prediksi: Teknologi Informasi",
        bg="#d4edda",
        fg="#155724"
    )
    
    # Menampilkan pesan pop-up sukses
    messagebox.showinfo("Sukses", "Prediksi Berhasil!\nProdi Pilihan Anda: Teknologi Informasi")

# Membuat jendela utama (Main Window)
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("480x600")
root.configure(bg="#f8f9fa")

# 1. Label Judul Aplikasi
label_judul = tk.Label(
    root,
    text="Aplikasi Prediksi Prodi Pilihan",
    font=("Arial", 16, "bold"),
    bg="#f8f9fa",
    fg="#333333"
)
label_judul.pack(pady=15)

# Frame untuk menampung 10 input nilai agar lebih rapi (menggunakan LabelFrame)
frame_input = tk.LabelFrame(
    root,
    text=" Masukkan Nilai 10 Mata Pelajaran ",
    font=("Arial", 10, "bold"),
    bg="#ffffff",
    fg="#0056b3",
    padx=15,
    pady=10
)
frame_input.pack(padx=20, pady=5, fill="both", expand=True)

# Daftar 10 mata pelajaran
mata_pelajaran = [
    "Matematika", "Bahasa Indonesia", "Bahasa Inggris", "Fisika", "Kimia",
    "Biologi", "Ekonomi", "Sosiologi", "Geografi", "Informatika"
]

entry_list = []

# 2. Membuat 10 input nilai mata pelajaran menggunakan Grid layout
for i, mp in enumerate(mata_pelajaran):
    lbl = tk.Label(frame_input, text=f"{mp}:", bg="#ffffff", font=("Arial", 9), anchor="w")
    lbl.grid(row=i, column=0, sticky="w", pady=4, padx=5)
    
    ent = tk.Entry(frame_input, width=15, font=("Arial", 9), bd=2, relief=tk.GROOVE)
    ent.grid(row=i, column=1, pady=4, padx=5)
    entry_list.append(ent)

# 3. Button bertuliskan "Hasil Prediksi"
btn_prediksi = tk.Button(
    root,
    text="Hasil Prediksi",
    command=hitung_prediksi,
    font=("Arial", 11, "bold"),
    bg="#007bff",
    fg="white",
    activebackground="#0056b3",
    activeforeground="white",
    padx=15,
    pady=6,
    cursor="hand2"
)
btn_prediksi.pack(pady=15)

# 4. Label luaran hasil prediksi
label_luaran = tk.Label(
    root,
    text="Hasil Prediksi: (Belum diproses)",
    font=("Arial", 11, "bold"),
    bg="#e2e3e5",
    fg="#383d41",
    width=40,
    height=2,
    relief=tk.RIDGE
)
label_luaran.pack(pady=(0, 20))

# Menjalankan aplikasi utama
root.mainloop()