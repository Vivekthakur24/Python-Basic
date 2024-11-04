import tkinter as tk
import random

# List of possible colors
colors = ['Red', 'Blue', 'Green', 'Pink', 'Black', 'Yellow', 'Orange', 'White', 'Purple', 'Brown']
score = 0
time_left = 30

def start_game(event):
    if time_left == 30:
        countdown()
    next_color()

def next_color():
    global score
    global time_left

    if time_left > 0:
        entry.focus_set()

        if entry.get().lower() == colors[1].lower():
            score += 1

        entry.delete(0, tk.END)

        random.shuffle(colors)

        label.config(fg=str(colors[1]), text=str(colors[0]))

        score_label.config(text="Score: " + str(score))

def countdown():
    global time_left

    if time_left > 0:
        time_left -= 1
        time_label.config(text="Time left: " + str(time_left))
        time_label.after(1000, countdown)
    else:
        entry.config(state='disabled')

# Setup the main window
root = tk.Tk()
root.title("Color Game")
root.geometry("375x200")

instructions = tk.Label(root, text="Type in the color of the words, not the word text!", font=('Helvetica', 12))
instructions.pack()

score_label = tk.Label(root, text="Press Enter to start", font=('Helvetica', 12))
score_label.pack()

time_label = tk.Label(root, text="Time left: " + str(time_left), font=('Helvetica', 12))
time_label.pack()

label = tk.Label(root, font=('Helvetica', 60))
label.pack()

entry = tk.Entry(root, font=('Helvetica', 18))
entry.pack()
entry.bind('<Return>', start_game)
entry.focus_set()

root.mainloop()


