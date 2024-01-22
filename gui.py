# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 16:49:04 2024

@author: asus
"""

import tkinter as tk
import subprocess

def run_python_script():
    # Belirtilen Python betiğini çalıştır
    subprocess.run(["python", "C://Users//asus//.spyder-py3//age_gender_detection.py"])

# Ana pencere oluştur
root = tk.Tk()
root.title("Yaşına Göre Sisteme Giriş")

# Form yüksekliğini ve genişliğini ayarla
form_width = 500
form_height = 500
root.geometry(f"{form_width}x{form_height}")


# Buton
button_run_script = tk.Button(root, text="Sisteme Giriş ", command=run_python_script)
button_run_script.pack(pady=20)

# Pencereyi çalıştır
root.mainloop()
