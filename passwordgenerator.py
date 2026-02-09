import tkinter as tk
import random
import string
from tkinter import messagebox

# ---------- FUNCTION ----------
def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Error", "Enter a valid length")
            return
    except:
        messagebox.showerror("Error", "Length must be a number")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))

    result_entry.delete(0, tk.END)
    result_entry.insert(0, password)

def copy_password():
    password = result_entry.get()
    if password == "":
        messagebox.showwarning("Warning", "No password to copy")
        return
    app.clipboard_clear()
    app.clipboard_append(password)
    messagebox.showinfo("Copied", "Password copied to clipboard")

# ---------- GUI ----------
app = tk.Tk()
app.title("Password Generator")
app.geometry("400x320")
app.resizable(False, False)

# Dark mode colors
bg_color = "#1e1e1e"
fg_color = "#ffffff"
entry_bg = "#2d2d2d"
btn_color = "#3a86ff"

app.configure(bg=bg_color)

# ---------- UI ELEMENTS ----------
title = tk.Label(app, text="Password Generator", font=("Arial", 18, "bold"),
                 bg=bg_color, fg=fg_color)
title.pack(pady=10)

length_label = tk.Label(app, text="Password Length:", bg=bg_color, fg=fg_color)
length_label.pack()

length_entry = tk.Entry(app, width=20, bg=entry_bg, fg=fg_color, insertbackground=fg_color)
length_entry.pack(pady=5)

generate_btn = tk.Button(app, text="Generate Password", bg=btn_color, fg="white",
                         width=20, command=generate_password)
generate_btn.pack(pady=10)

result_label = tk.Label(app, text="Generated Password:", bg=bg_color, fg=fg_color)
result_label.pack()

result_entry = tk.Entry(app, width=35, bg=entry_bg, fg=fg_color, insertbackground=fg_color)
result_entry.pack(pady=5)

copy_btn = tk.Button(app, text="Copy Password", bg="#06d6a0", fg="black",
                     width=20, command=copy_password)
copy_btn.pack(pady=10)

app.mainloop()
