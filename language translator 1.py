import tkinter as tk
from googletrans import Translator, LANGUAGES

class EnglishToAnyTranslator:
    def __init__(self, root):
        self.root = root
        self.root.title("English to Any Language Translator")
        self.root.geometry("800x400")
        self.root.configure(background="lightblue")

        # Create input field for English text
        self.english_label = tk.Label(root, text="English Text:", bg="lightblue", fg="black", font=("Arial", 18))
        self.english_label.pack()
        self.english_text = tk.Text(root, height=10, width=80, font=("Arial", 18))
        self.english_text.pack()

        # Create dropdown menu for target language
        self.language_label = tk.Label(root, text="Select Target Language:", bg="lightblue", fg="black", font=("Arial", 18))
        self.language_label.pack()
        self.language_var = tk.StringVar()
        language_options = [f"{lang} - {LANGUAGES[lang]}" for lang in LANGUAGES]
        self.language_menu = tk.OptionMenu(root, self.language_var, *language_options)
        self.language_menu.pack()

        # Create button to translate
        self.translate_button = tk.Button(root, text="Translate", command=self.translate, bg="green", fg="white", font=("Arial", 24))
        self.translate_button.pack(pady=20)

        # Create output field for translated text
        self.translated_label = tk.Label(root, text="Translated Text:", bg="lightblue", fg="black", font=("Arial", 18))
        self.translated_label.pack()
        self.translated_text = tk.Text(root, height=10, width=80, font=("Arial", 18))
        self.translated_text.pack()

    def translate(self):
        try:
            # Get English text from input field
            english_text = self.english_text.get("1.0", "end-1c")

            # Get target language from dropdown menu
            target_language_full = self.language_var.get()
            target_language = target_language_full.split(" - ")[0]

            # Create a Google Translate object
            translator = Translator()

            # Translate English text to target language
            translated_text = translator.translate(english_text, dest=target_language).text

            # Display translated text in output field
            self.translated_text.delete("1.0", "end")
            self.translated_text.insert("1.0", translated_text)
        except Exception as e:
            self.translated_text.delete("1.0", "end")
            self.translated_text.insert("1.0", "Error: " + str(e))

if __name__ == "__main__":
    root = tk.Tk()
    translator = EnglishToAnyTranslator(root)
    root.mainloop()
