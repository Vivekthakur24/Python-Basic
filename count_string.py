#program to count the string
strings = ["apple", "banana", "cherry", "orange"]
string_count = 0
for item in strings:
  if isinstance(item, str):
    string_count += 1
print(f"The list contains {string_count} strings.")
