import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    password_length = int(entry_password_length.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(password_length))
    entry_generated_password.delete(0, tk.END)
    entry_generated_password.insert(0, password)

def reset_fields():
    entry_username.delete(0, tk.END)
    entry_password_length.delete(0, tk.END)
    entry_generated_password.delete(0, tk.END)

def submit_data():
    username = entry_username.get()
    password_length = entry_password_length.get()

    if username and password_length:
        messagebox.showinfo("Success", "Data submitted successfully!")
    else:
        messagebox.showerror("Error", "Please enter both username and password length.")


root = tk.Tk()
root.title("User Data Entry")

label_username = tk.Label(root, text="Username:")
label_password_length = tk.Label(root, text="Password Length:")
label_generated_password = tk.Label(root, text="Generated Password:")

entry_username = tk.Entry(root)
entry_password_length = tk.Entry(root)
entry_generated_password = tk.Entry(root)

button_generate_password = tk.Button(root, text="Generate Password", command=generate_password)
button_reset = tk.Button(root, text="Reset", command=reset_fields)
button_submit = tk.Button(root, text="Submit", command=submit_data)

label_username.grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_username.grid(row=0, column=1, padx=10, pady=10)
label_password_length.grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_password_length.grid(row=1, column=1, padx=10, pady=10)
label_generated_password.grid(row=2, column=0, padx=10, pady=10, sticky="w")
entry_generated_password.grid(row=2, column=1, padx=10, pady=10)
button_generate_password.grid(row=3, column=1, padx=10, pady=10)
button_reset.grid(row=3, column=2, padx=10, pady=20)
button_submit.grid(row=3, column=0, padx=10, pady=20)

root.mainloop()
