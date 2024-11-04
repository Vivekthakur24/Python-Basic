"""Finds Pythagorean triplets under a given limit."""
def find_triplets(limit):
  triplets = []
  for a in range(1, limit):
    for b in range(a, limit):
      c_squared = a**2 + b**2
      c = int(c_squared**0.5)
      if c <= limit and c**2 == c_squared:
        triplets.append((a, b, c))
  return triplets
limit = 50   # Set the limit
triplets = find_triplets(limit)# Find Pythagorean triplets
if triplets:     # Print the triplets
  for a, b, c in triplets:
    print(f"({a}, {b}, {c})")
else:
  print("No Pythagorean triplets found under the limit.")
