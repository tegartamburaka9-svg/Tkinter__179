import tkinter as tk
from tkinter import messagebox


def aksi_tombol():
    nama = entry_nama.get()
    pilihan = var_radio.get()
    skala = scale_nilai.get()
    
    pesan_text = text_area.get("1.0", tk.END).strip()
    
    info = (
        f"Nama: {nama if nama else '(Kosong)'}\n"
        f"Radio Pilihan: {pilihan}\n"
        f"Skala Nilai: {skala}\n"
        f"Pesan Text: {pesan_text[:30]}..."
    )
    messagebox.showinfo("Hasil Input Komponen", info)