import tkinter as tk
from googletrans import Translator, LANGUAGES

class FlexibleTranslator:
    def __init__(self, root):
        self.root = root
        self.root.title("Flexible Language Translator")
        self.root.geometry("800x450")
        self.root.configure(background="lightblue")

        # Create input field for English text
        self.english_label = tk.Label(root, text="English Text:", bg="lightblue", fg="black", font=("Arial", 14))
        self.english_label.pack(pady=10)
        self.english_text = tk.Text(root, height=8, width=60, font=("Arial", 14))
        self.english_text.pack(pady=10)

        # Create dropdown for language selection
        self.language_label = tk.Label(root, text="Select Language:", bg="lightblue", fg="black", font=("Arial", 14))
        self.language_label.pack(pady=10)
        self.languages = LANGUAGES  # Use the LANGUAGES dictionary from googletrans
        self.language_var = tk.StringVar(root)
        self.language_var.set("hindi")  # Default value
        self.language_menu = tk.OptionMenu(root, self.language_var, *self.languages.values())
        self.language_menu.config(font=("Arial", 12))
        self.language_menu.pack(pady=10)

        # Create button to translate
        self.translate_button = tk.Button(root, text="Translate", command=self.translate, bg="green", fg="white", font=("Arial", 18))
        self.translate_button.pack(pady=20)

        # Create output field for translated text
        self.translated_label = tk.Label(root, text="Translated Text:", bg="lightblue", fg="black", font=("Arial", 14))
        self.translated_label.pack(pady=10)
        self.translated_text = tk.Text(root, height=8, width=60, font=("Arial", 14))
        self.translated_text.pack(pady=10)

    def translate(self):
        try:
            # Get English text from input field
            english_text = self.english_text.get("1.0", "end-1c").strip()

            if not english_text:
                self.translated_text.delete("1.0", "end")
                self.translated_text.insert("1.0", "Please enter some text to translate.")
                return

            # Get selected language
            selected_language_name = self.language_var.get()
            selected_language_code = [code for code, name in self.languages.items() if name == selected_language_name][0]

            # Create a Translator object
            translator = Translator()

            # Translate English text to the selected language
            translated_text = translator.translate(english_text, dest=selected_language_code).text

            # Display translated text in output field
            self.translated_text.delete("1.0", "end")
            self.translated_text.insert("1.0", translated_text)
        except Exception as e:
            self.translated_text.delete("1.0", "end")
            self.translated_text.insert("1.0", "Error: " + str(e))

if __name__ == "__main__":
    root = tk.Tk()
    translator = FlexibleTranslator(root)
    root.mainloop()
