import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk

def generate_qr():
    name = name_entry.get()
    if not name:
        messagebox.showerror("Error", "Name field cannot be empty!")
        return

    # Generate QR Code
    qr_text = f"NAME:{name}"
    qr_img = qrcode.make(qr_text)
    
    # Save QR Code
    qr_img.save(f"{name}.png")
    messagebox.showinfo("Success", f"QR Code Generated and Saved as {name}.png")
    
    # Display QR Code in GUI
    qr_img_display = qr_img.resize((200, 200))
    qr_img_tk = ImageTk.PhotoImage(qr_img_display)
    qr_label.config(image=qr_img_tk)
    qr_label.image = qr_img_tk

# GUI Setup
app = tk.Tk()
app.title("QR Code Generator")
app.geometry("400x400")

# Title Label
title_label = tk.Label(app, text="QR Code Generator", font=("Arial", 16))
title_label.pack(pady=10)

# Input Label and Entry
name_label = tk.Label(app, text="Enter Your Name:", font=("Arial", 12))
name_label.pack(pady=5)

name_entry = tk.Entry(app, font=("Arial", 12), width=30)
name_entry.pack(pady=5)

# Generate Button
generate_button = tk.Button(app, text="Generate QR Code", command=generate_qr, font=("Arial", 12), bg="blue", fg="white")
generate_button.pack(pady=10)

# QR Code Display Label
qr_label = tk.Label(app)
qr_label.pack(pady=20)

# Run the Application
app.mainloop()
