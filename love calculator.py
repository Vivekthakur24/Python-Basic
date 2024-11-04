import tkinter as tk
import random

def calculate_love():
    name1 = name1_entry.get()
    name2 = name2_entry.get()
    love_score = random.randint(0, 100)
    if love_score < 30:
        result_label.config(text=f"Your love score is {love_score}. You go together like oil and water.")
    elif love_score < 50:
        result_label.config(text=f"Your love score is {love_score}. You're alright together.")
    elif love_score < 70:
        result_label.config(text=f"Your love score is {love_score}. You're a good match.")
    else:
        result_label.config(text=f"Your love score is {love_score}. You're meant to be!")

root = tk.Tk()
root.title("Love Calculator")
root.configure(background='#C6E2B5')  # light green background

# Create labels and entries
name1_label = tk.Label(root, text="Enter your name:", font=('Helvetica', 14), bg='#C6E2B5')
name1_label.pack()

name1_entry = tk.Entry(root, width=25, font=('Helvetica', 14))
name1_entry.pack()

name2_label = tk.Label(root, text="Enter your partner's name:", font=('Helvetica', 14), bg='#C6E2B5')
name2_label.pack()

name2_entry = tk.Entry(root, width=25, font=('Helvetica', 14))
name2_entry.pack()

calculate_button = tk.Button(root, text="Calculate Love", command=calculate_love, font=('Helvetica', 16), fg='white', bg='red')
calculate_button.pack(pady=10)  # increase button size and move it down a bit

result_label = tk.Label(root, text="", font=('Helvetica', 14), bg='#C6E2B5')
result_label.pack()

root.mainloop()

