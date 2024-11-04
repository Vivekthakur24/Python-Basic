dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'b': 4, 'd': 5}
merged_dict = {}
for key in dict1.keys() | dict2.keys():
  if key in dict1:
    merged_dict[key] = dict1[key]
  if key in dict2:
    merged_dict[key] = dict2[key]

print(f"Merged dictionary: {merged_dict}")
