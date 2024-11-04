# #program to list creation
# numbers = [1, 2, 3, 4, 5]
# squares = []
# for num in numbers:
#  squares.append(num * num)
# print(f"List of squares: {squares}")
import re
txt= "I am a student "
print (re.search("student" ,txt))
print (re.findall("student" ,txt))
print (re.split("student",txt))
print (re.search("student" ,txt))