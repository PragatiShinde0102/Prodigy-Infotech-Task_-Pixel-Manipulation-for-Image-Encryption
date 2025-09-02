import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

# Pixel manipulation function
def process_image(file_path, key, mode):
    img = Image.open(file_path)
    pixels = img.load()
    
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            
            if mode == "encrypt":
                pixels[i, j] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)
            elif mode == "decrypt":
                pixels[i, j] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)
    
    return img

# Browse image
def browse_image():
    global file_path
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")]
    )
    if file_path:
        img = Image.open(file_path)
        img.thumbnail((300, 300))
        img_display = ImageTk.PhotoImage(img)
        panel.config(image=img_display)
        panel.image = img_display
        messagebox.showinfo("Selected", f"Selected image: {os.path.basename(file_path)}")

# Encrypt image
def encrypt_image():
    if not file_path:
        messagebox.showerror("Error", "Please select an image first.")
        return
    try:
        key = int(key_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Enter a valid integer key.")
        return
    
    img = process_image(file_path, key, "encrypt")
    save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG files", "*.png")])
    if save_path:
        img.save(save_path)
        messagebox.showinfo("Success", f"Encrypted image saved as {save_path}")

# Decrypt image
def decrypt_image():
    if not file_path:
        messagebox.showerror("Error", "Please select an image first.")
        return
    try:
        key = int(key_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Enter a valid integer key.")
        return
    
    img = process_image(file_path, key, "decrypt")
    save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG files", "*.png")])
    if save_path:
        img.save(save_path)
        messagebox.showinfo("Success", f"Decrypted image saved as {save_path}")

# GUI setup
root = tk.Tk()
root.title("Image Encryption & Decryption")
root.geometry("500x600")
root.config(bg="#2E3B55")

file_path = None

title = tk.Label(root, text="🔒 Image Encryption Tool", font=("Arial", 18, "bold"), fg="white", bg="#2E3B55")
title.pack(pady=10)

browse_btn = tk.Button(root, text="Browse Image", command=browse_image, bg="#4CAF50", fg="white", font=("Arial", 12), width=20)
browse_btn.pack(pady=10)

panel = tk.Label(root, bg="#2E3B55")
panel.pack(pady=10)

key_label = tk.Label(root, text="Enter Key (number):", font=("Arial", 12), fg="white", bg="#2E3B55")
key_label.pack(pady=5)

key_entry = tk.Entry(root, font=("Arial", 12), justify="center")
key_entry.pack(pady=5)

encrypt_btn = tk.Button(root, text="Encrypt Image", command=encrypt_image, bg="#2196F3", fg="white", font=("Arial", 12), width=20)
encrypt_btn.pack(pady=10)

decrypt_btn = tk.Button(root, text="Decrypt Image", command=decrypt_image, bg="#f44336", fg="white", font=("Arial", 12), width=20)
decrypt_btn.pack(pady=10)

root.mainloop()
