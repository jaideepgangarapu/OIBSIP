import random
import string
import tkinter as tk
from tkinter import messagebox

# Function to generate password
def generate_password():
    length = length_entry.get()

    if not length.isdigit():
        messagebox.showerror("Error", "Please enter a valid number!")
        return

    length = int(length)

    if length <= 0:
        messagebox.showerror("Error", "Password length must be greater than 0!")
        return

    characters = ""

    if var_upper.get():
        characters += string.ascii_uppercase

    if var_lower.get():
        characters += string.ascii_lowercase

    if var_digits.get():
        characters += string.digits

    if var_symbols.get():
        characters += string.punctuation

    if characters == "":
        messagebox.showerror("Error", "Select at least one character type!")
        return

    password = ''.join(random.choice(characters) for _ in range(length))

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Function to copy password
def copy_password():
    password = password_entry.get()

    if password == "":
        messagebox.showwarning("Warning", "No password generated!")
        return

    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()

    messagebox.showinfo("Copied", "Password copied to clipboard!")

def main():
    global root, length_entry, var_upper, var_lower, var_digits, var_symbols, password_entry

    # Main Window
    root = tk.Tk()
    root.title("Random Password Generator")
    root.geometry("500x450")
    root.config(bg="#1e1e2f")

    # Heading
    title = tk.Label(
        root,
        text="Secure Password Generator",
        font=("Arial", 20, "bold"),
        bg="#1e1e2f",
        fg="white"
    )
    title.pack(pady=20)

    # Password Length
    length_label = tk.Label(
        root,
        text="Enter Password Length:",
        font=("Arial", 12),
        bg="#1e1e2f",
        fg="white"
    )
    length_label.pack()

    length_entry = tk.Entry(font=("Arial", 14), justify="center")
    length_entry.pack(pady=10)

    # Checkboxes
    var_upper = tk.IntVar()
    var_lower = tk.IntVar()
    var_digits = tk.IntVar()
    var_symbols = tk.IntVar()

    tk.Checkbutton(
        root,
        text="Include Uppercase Letters",
        variable=var_upper,
        bg="#1e1e2f",
        fg="white",
        selectcolor="#333333",
        font=("Arial", 11)
    ).pack(anchor="w", padx=100)

    tk.Checkbutton(
        root,
        text="Include Lowercase Letters",
        variable=var_lower,
        bg="#1e1e2f",
        fg="white",
        selectcolor="#333333",
        font=("Arial", 11)
    ).pack(anchor="w", padx=100)

    tk.Checkbutton(
        root,
        text="Include Numbers",
        variable=var_digits,
        bg="#1e1e2f",
        fg="white",
        selectcolor="#333333",
        font=("Arial", 11)
    ).pack(anchor="w", padx=100)

    tk.Checkbutton(
        root,
        text="Include Symbols",
        variable=var_symbols,
        bg="#1e1e2f",
        fg="white",
        selectcolor="#333333",
        font=("Arial", 11)
    ).pack(anchor="w", padx=100)

    # Generate Button
    generate_btn = tk.Button(
        root,
        text="Generate Password",
        command=generate_password,
        font=("Arial", 13, "bold"),
        bg="#4CAF50",
        fg="white",
        padx=10,
        pady=5
    )
    generate_btn.pack(pady=20)

    # Password Display
    password_entry = tk.Entry(
        root,
        font=("Arial", 14),
        justify="center",
        width=30
    )
    password_entry.pack(pady=10)

    # Copy Button
    copy_btn = tk.Button(
        root,
        text="Copy Password",
        command=copy_password,
        font=("Arial", 12, "bold"),
        bg="#2196F3",
        fg="white",
        padx=10,
        pady=5
    )
    copy_btn.pack(pady=10)

# Run Application
if __name__ == "__main__":
    main()