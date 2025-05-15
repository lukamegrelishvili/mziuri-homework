import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
from datetime import datetime

# === Генерация пароля ===
def generate_password():
    length = length_var.get()

    charset = ''
    if use_letters.get():
        charset += string.ascii_letters
    if use_digits.get():
        charset += string.digits
    if use_symbols.get():
        charset += string.punctuation

    if not charset:
        result_label.config(text="Выбери хотя бы 1 тип!")
        return

    password = ''.join(random.choice(charset) for _ in range(length))
    result_label.config(text=password)

    # Анимация
    result_label.config(fg="#ff9800")
    result_label.after(150, lambda: result_label.config(fg="#4caf50"))

# === Сохранение в файл ===
def save_password():
    password = result_label.cget("text")
    if not password or "Выбери" in password:
        messagebox.showinfo("Упс", "Сначала сгенерируй пароль")
        return

    with open("saved_passwords.txt", "a", encoding="utf-8") as file:
        file.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {password}\n")
    messagebox.showinfo("Сохранено", "Пароль сохранён в файл!")

# === Окно ===
root = tk.Tk()
root.title("🔐 Генератор паролей")
root.geometry("450x450")
root.configure(bg="#1e1e2f")
root.resizable(False, False)

# === Стили ===
style = ttk.Style()
style.theme_use("default")
style.configure("TButton",
                font=("Segoe UI", 11),
                padding=10,
                background="#4caf50",
                foreground="white")
style.map("TButton",
          background=[("active", "#45a049")])

# === Заголовок ===
tk.Label(root, text="🔑 Генератор безопасных паролей", font=("Segoe UI", 16, "bold"),
         bg="#1e1e2f", fg="white").pack(pady=20)

# === Настройки пароля ===
settings_frame = tk.Frame(root, bg="#1e1e2f")
settings_frame.pack(pady=10)

# Ползунок длины
tk.Label(settings_frame, text="Длина пароля:", bg="#1e1e2f", fg="white", font=("Segoe UI", 10)).grid(row=0, column=0, padx=5, sticky="w")
length_var = tk.IntVar(value=12)
length_slider = ttk.Scale(settings_frame, from_=4, to=32, variable=length_var, orient="horizontal", length=200)
length_slider.grid(row=0, column=1, padx=10)

# Чекбоксы
use_letters = tk.BooleanVar(value=True)
use_digits = tk.BooleanVar(value=True)
use_symbols = tk.BooleanVar(value=True)

tk.Checkbutton(settings_frame, text="Буквы", variable=use_letters, bg="#1e1e2f", fg="white", selectcolor="#1e1e2f", font=("Segoe UI", 10)).grid(row=1, column=0, sticky="w")
tk.Checkbutton(settings_frame, text="Цифры", variable=use_digits, bg="#1e1e2f", fg="white", selectcolor="#1e1e2f", font=("Segoe UI", 10)).grid(row=1, column=1, sticky="w")
tk.Checkbutton(settings_frame, text="Символы", variable=use_symbols, bg="#1e1e2f", fg="white", selectcolor="#1e1e2f", font=("Segoe UI", 10)).grid(row=1, column=2, sticky="w")

# === Кнопка генерации ===
ttk.Button(root, text="Сгенерировать пароль", command=generate_password).pack(pady=15)

# === Результат ===
result_label = tk.Label(root, text="", font=("Courier New", 14, "bold"), fg="#4caf50", bg="#1e1e2f")
result_label.pack(pady=10)

# === Кнопка сохранения ===
ttk.Button(root, text="💾 Сохранить пароль", command=save_password).pack(pady=10)

# === Подпись ===
tk.Label(root, text="Сделано с ❤️ на Python", font=("Segoe UI", 9), bg="#1e1e2f", fg="#aaaaaa").pack(side="bottom", pady=10)

# === Запуск ===
root.mainloop()
