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

def buka_toplevel():
    top = tk.Toplevel(root)
    top.title("Jendela Toplevel (Sub-Window)")
    top.geometry("250x150")
    top.configure(bg="#e8f5e9")
    
    tk.Label(top, text="Ini adalah Jendela Toplevel!", bg="#e8f5e9", font=("Arial", 10, "bold")).pack(pady=20)
    tk.Button(top, text="Tutup Jendela", command=top.destroy).pack(pady=10)
root = tk.Tk()
root.title("Gabungan 15 Widget Tkinter Lengkap")
root.geometry("650x750")
root.configure(bg="#f5f5f5")
canvas = tk.Canvas(root, bg="#1976d2", height=50, highlightthickness=0)
canvas.pack(fill=tk.X)
canvas.create_text(325, 25, text="DEMONSTRASI 15 WIDGET TKINTER", fill="white", font=("Arial", 12, "bold"))
main_frame = tk.Frame(root, bg="#f5f5f5")
main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
