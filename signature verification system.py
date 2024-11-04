import tkinter as tk
from tkinter import filedialog, messagebox as mb
from PIL import Image, ImageTk
import numpy as np

# Function to browse and display the first image
def browse_image1():
    filepath = filedialog.askopenfilename(title="Select Image 1", filetypes=[("Image Files", ".jpg .png .jpeg .bmp")])
    if filepath:
        img1 = Image.open(filepath)
        img1 = img1.resize((400, 300), Image.ANTIALIAS)  # Increase image size
        img1_tk = ImageTk.PhotoImage(img1)
        img1_label.config(image=img1_tk)
        img1_label.image = img1_tk
        img1.save("image1.jpg")

# Function to browse and display the second image
def browse_image2():
    filepath = filedialog.askopenfilename(title="Select Image 2", filetypes=[("Image Files", ".jpg .png .jpeg .bmp")])
    if filepath:
        img2 = Image.open(filepath)
        img2 = img2.resize((400, 300), Image.ANTIALIAS)  # Increase image size
        img2_tk = ImageTk.PhotoImage(img2)
        img2_label.config(image=img2_tk)
        img2_label.image = img2_tk
        img2.save("image2.jpg")

# Function to verify signatures
def verify_signatures():
    img1_array = np.array(Image.open("image1.jpg"))
    img2_array = np.array(Image.open("image2.jpg"))
    difference = np.abs(img1_array - img2_array)
    accuracy = 1 - (np.sum(difference) / (img1_array.size * 255))
    if accuracy >= 0.5:
        accuracy_label.config(text=f"Signatures Match with {accuracy:.2%} accuracy", fg="green", font=("Helvetica", 16, "bold"))
    else:
        accuracy_label.config(text=f"Signatures Do Not Match with {accuracy:.2%} accuracy", fg="red", font=("Helvetica", 16, "bold"))

# Set up the main application window
root = tk.Tk()
root.title("Signature Verification System by TECH GUARDIAN SOCIETY")
root.configure(background='blue')  # Set blue background
root.configure(borderwidth=10, highlightbackground="blue", highlightthickness=10)  # Add blue border

# Create and place the widgets
img1_label = tk.Label(root, bg="blue")
img1_label.place(x=100, y=50)  # Adjust coordinates to position img1_label at the top with some space

img2_label = tk.Label(root, bg="blue")
img2_label.place(x=800, y=50)  # Adjust coordinates to position img2_label at the top with some space and more distance from img1_label

img1_button = tk.Button(root, text="Browse Image 1", command=browse_image1, fg="red", bg="black", bd=3, relief="raised", width=20, height=2, font=("Helvetica", 12))
img1_button.place(x=100, y=380)  # Adjust coordinates and size of button

img2_button = tk.Button(root, text="Browse Image 2", command=browse_image2, fg="red", bg="black", bd=3, relief="raised", width=20, height=2, font=("Helvetica", 12))
img2_button.place(x=800, y=380)  # Adjust coordinates and size of button

verify_button = tk.Button(root, text="Verify Signatures", command=verify_signatures, fg="red", bg="black", width=30, height=2, font=("Helvetica", 14, "bold"))
verify_button.pack(pady=20, side="bottom")  # Place verify_button at the bottom using pack

accuracy_label = tk.Label(root, text="", fg="white", bg="black", font=("Helvetica", 16, "bold"))
accuracy_label.pack(pady=20, side="bottom")  # Place accuracy_label below verify_button

# Run the application
root.mainloop()

import tkinter as tk
from tkinter import filedialog, messagebox as mb
from PIL import Image, ImageTk
import numpy as np

# Function to browse and display the first image
def browse_image1():
    filepath = filedialog.askopenfilename(title="Select Image 1", filetypes=[("Image Files", ".jpg .png .jpeg .bmp")])
    if filepath:
        img1 = Image.open(filepath)
        img1 = img1.resize((400, 300), Image.ANTIALIAS)  # Increase image size
        img1_tk = ImageTk.PhotoImage(img1)
        img1_label.config(image=img1_tk)
        img1_label.image = img1_tk
        img1.save("image1.jpg")

# Function to browse and display the second image
def browse_image2():
    filepath = filedialog.askopenfilename(title="Select Image 2", filetypes=[("Image Files", ".jpg .png .jpeg .bmp")])
    if filepath:
        img2 = Image.open(filepath)
        img2 = img2.resize((400, 300), Image.ANTIALIAS)  # Increase image size
        img2_tk = ImageTk.PhotoImage(img2)
        img2_label.config(image=img2_tk)
        img2_label.image = img2_tk
        img2.save("image2.jpg")

# Function to verify signatures
def verify_signatures():
    img1_array = np.array(Image.open("image1.jpg"))
    img2_array = np.array(Image.open("image2.jpg"))
    difference = np.abs(img1_array - img2_array)
    accuracy = 1 - (np.sum(difference) / (img1_array.size * 255))
    if accuracy >= 0.5:
        accuracy_label.config(text=f"Signatures Match with {accuracy:.2%} accuracy", fg="green", font=("Helvetica", 16, "bold"))
    else:
        accuracy_label.config(text=f"Signatures Do Not Match with {accuracy:.2%} accuracy", fg="red", font=("Helvetica", 16, "bold"))

# Set up the main application window
root = tk.Tk()
root.title("Signature Verification System by TECH GUARDIAN SOCIETY")
root.configure(background='blue')  # Set blue background
root.configure(borderwidth=10, highlightbackground="blue", highlightthickness=10)  # Add blue border

# Create and place the widgets
img1_label = tk.Label(root, bg="blue")
img1_label.place(x=100, y=50)  # Adjust coordinates to position img1_label at the top with some space

img2_label = tk.Label(root, bg="blue")
img2_label.place(x=800, y=50)  # Adjust coordinates to position img2_label at the top with some space and more distance from img1_label

img1_button = tk.Button(root, text="Browse Image 1", command=browse_image1, fg="red", bg="black", bd=3, relief="raised", width=20, height=2, font=("Helvetica", 12))
img1_button.place(x=100, y=380)  # Adjust coordinates and size of button

img2_button = tk.Button(root, text="Browse Image 2", command=browse_image2, fg="red", bg="black", bd=3, relief="raised", width=20, height=2, font=("Helvetica", 12))
img2_button.place(x=800, y=380)  # Adjust coordinates and size of button

verify_button = tk.Button(root, text="Verify Signatures", command=verify_signatures, fg="red", bg="black", width=30, height=2, font=("Helvetica", 14, "bold"))
verify_button.pack(pady=20, side="bottom")  # Place verify_button at the bottom using pack

accuracy_label = tk.Label(root, text="", fg="white", bg="black", font=("Helvetica", 16, "bold"))
accuracy_label.pack(pady=20, side="bottom")  # Place accuracy_label below verify_button

# Run the application
root.mainloop()

