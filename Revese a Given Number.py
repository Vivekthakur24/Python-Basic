#Reverse the GIven number
def reverse_number(num):
 reversed_num = 0
 while num > 0:
   digit = num % 10
   reversed_num = reversed_num * 10 + digit
   num //= 10
 return reversed_num


number = 12345
reversed_number = reverse_number(number)
print(f"The reversed number of {number} is {reversed_number}")
