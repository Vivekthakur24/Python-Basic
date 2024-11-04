# program go remove the vowels from the sectence
text = (input("enter the sentence to remove vowel: "))
consonants = "bcdfghjklmnpqrstvwxyz "
result = ""
for char in text:
  if char in consonants:
    result += char
print(f"Text without vowels and punctuation: {result}")
