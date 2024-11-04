# To find reverse number
num = int(input('enter the number'))
original_num = num
reversed_num = 0
while num > 0:
  digit = num % 10
  reversed_num = reversed_num * 10 + digit
  num //= 10
print(f"The reversed number {original_num } of  is {reversed_num}")
