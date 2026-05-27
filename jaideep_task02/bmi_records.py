import tkinter as tk
from tkinter import messagebox
import csv
from datetime import datetime

try:
    import matplotlib.pyplot as plt # type: ignore
except ImportError:
    plt = None

# ---------------- BMI Calculation ---------------- #

def calculate_bmi():
    try:
        name = entry_name.get()

        weight = float(entry_weight.get())
        height = float(entry_height.get())

        if weight <= 0 or height <= 0:
            messagebox.showerror("Error", "Height and Weight must be positive values")
            return

        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)

        category = get_category(bmi)

        result_label.config(
            text=f"Name: {name}\nBMI: {bmi}\nCategory: {category}"
        )

        save_data(name, weight, height, bmi, category)

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")


# ---------------- BMI Category ---------------- #

def get_category(bmi):

    if bmi < 18.5:
        return "Underweight"

    elif bmi < 25:
        return "Normal Weight"

    elif bmi < 30:
        return "Overweight"

    else:
        return "Obese"


# ---------------- Save Data ---------------- #

def save_data(name, weight, height, bmi, category):

    with open("bmi_records.csv", mode="a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            datetime.now(),
            name,
            weight,
            height,
            bmi,
            category
        ])


# ---------------- Show Graph ---------------- #

def show_graph():

    if plt is None:
        messagebox.showerror(
            "Error",
            "matplotlib is not installed. Install it to view the BMI graph."
        )
        return

    bmi_values = []
    names = []

    try:
        with open("bmi_records.csv", mode="r") as file:

            reader = csv.reader(file)

            for row in reader:
                names.append(row[1])
                bmi_values.append(float(row[4]))

        if not bmi_values:
            raise ValueError("No BMI records")

        plt.figure(figsize=(8,5))
        plt.plot(names, bmi_values, marker='o')

        plt.title("BMI History")
        plt.xlabel("Users")
        plt.ylabel("BMI")

        plt.grid(True)
        plt.show()

    except Exception:
        messagebox.showinfo("Info", "No data available")


# ---------------- GUI Window ---------------- #

root = tk.Tk()

root.title("Smart BMI Calculator")
root.geometry("500x500")
root.config(bg="#E8F6F3")

title = tk.Label(
    root,
    text="BMI Calculator",
    font=("Arial", 22, "bold"),
    bg="#E8F6F3",
    fg="#117A65"
)

title.pack(pady=20)

# Name

tk.Label(root, text="Enter Name", bg="#E8F6F3",
         font=("Arial", 12)).pack()

entry_name = tk.Entry(root, width=30)
entry_name.pack(pady=5)

# Weight

tk.Label(root, text="Weight (kg)", bg="#E8F6F3",
         font=("Arial", 12)).pack()

entry_weight = tk.Entry(root, width=30)
entry_weight.pack(pady=5)

# Height

tk.Label(root, text="Height (m)", bg="#E8F6F3",
         font=("Arial", 12)).pack()

entry_height = tk.Entry(root, width=30)
entry_height.pack(pady=5)

# Buttons

calculate_btn = tk.Button(
    root,
    text="Calculate BMI",
    command=calculate_bmi,
    bg="#16A085",
    fg="white",
    width=20,
    font=("Arial", 12, "bold")
)

calculate_btn.pack(pady=15)

graph_btn = tk.Button(
    root,
    text="Show BMI Graph",
    command=show_graph,
    bg="#1F618D",
    fg="white",
    width=20,
    font=("Arial", 12, "bold")
)

graph_btn.pack(pady=10)

# Result

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 14, "bold"),
    bg="#E8F6F3",
    fg="#922B21"
)

result_label.pack(pady=20)

if __name__ == "__main__":
    root.mainloop()