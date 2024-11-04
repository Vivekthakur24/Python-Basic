#program to check pythagorean triplet
limit = int(input('enter the number'))

for a in range(1, limit):
  for b in range(a, limit):

    c_squared = a**2 + b**2

    if c_squared <= limit**2 and int(c_squared**0.5) ** 2 == c_squared:
      c = int(c_squared**0.5)
      print(f"Pythagorean triplet: ({a}, {b}, {c})")
