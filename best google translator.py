import tkinter as tk
from googletrans import Translator

class EnglishToHindiTranslator:
    def __init__(self, root):
        self.root = root
        self.root.title("English to Hindi Translator")
        self.root.geometry("800x400")  # Increased window size
        self.root.configure(background="lightblue")

        # Create input field for English text
        self.english_label = tk.Label(root, text="English Text:", bg="lightblue", fg="black", font=("Arial", 18))  # Increased font size
        self.english_label.pack()
        self.english_text = tk.Text(root, height=10, width=80, font=("Arial", 18))  # Increased input field size and font size
        self.english_text.pack()

        # Create button to translate
        self.translate_button = tk.Button(root, text="Translate to Hindi", command=self.translate, bg="green", fg="white", font=("Arial", 24))  # Increased font size and button size
        self.translate_button.pack(pady=20)  # Added padding to make the button more prominent

        # Create output field for Hindi text
        self.hindi_label = tk.Label(root, text="Hindi Text:", bg="lightblue", fg="black", font=("Arial", 18))  # Increased font size
        self.hindi_label.pack()
        self.hindi_text = tk.Text(root, height=10, width=80, font=("Arial", 18))  # Increased output field size and font size
        self.hindi_text.pack()

    def translate(self):
        try:
            # Get English text from input field
            english_text = self.english_text.get("1.0", "end-1c")

            # Create a Google Translate object
            translator = Translator()

            # Translate English text to Hindi
            hindi_text = translator.translate(english_text, dest="hi").text

            # Display Hindi text in output field
            self.hindi_text.delete("1.0", "end")
            self.hindi_text.insert("1.0", hindi_text)
        except Exception as e:
            self.hindi_text.delete("1.0", "end")
            self.hindi_text.insert("1.0", "Error: " + str(e))

if __name__ == "__main__":
    root = tk.Tk()
    translator = EnglishToHindiTranslator(root)
    root.mainloop()
