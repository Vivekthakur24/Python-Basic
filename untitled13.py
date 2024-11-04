import tkinter as tk
from datetime import datetime

def calculate_age():
    try:
        birth_date = birth_date_entry.get()
        birth_date = datetime.strptime(birth_date, "%d/%m/%Y")
        today = datetime.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        if age > 50:
            result_label.config(text=f"You are {age} years old. You are old.")
        else:
            result_label.config(text=f"You are {age} years old.")
    except ValueError:
        result_label.config(text="Invalid date format. Please use DD/MM/YYYY.")

root = tk.Tk()
root.title("Age Calculator")
root.configure(background='#C6E2B5')  # light green background

# Create labels and entries
birth_date_label = tk.Label(root, text="Enter your birth date (DD/MM/YYYY):", font=('Helvetica', 14), bg='#C6E2B5')
birth_date_label.pack()

birth_date_entry = tk.Entry(root, width=25, font=('Helvetica', 14))
birth_date_entry.pack()

calculate_button = tk.Button(root, text="Predict Age", command=calculate_age, font=('Helvetica', 16), fg='white', bg='red')
calculate_button.pack(pady=10)  # increase button size and move it down a bit

result_label = tk.Label(root, text="", font=('Helvetica', 14), bg='#C6E2B5')
result_label.pack()

root.mainloop()



