#program to shor the tuple in python
my_tuple = (3, 1, 4, 1, 5, 9)
sorted_list = []
for element in my_tuple:
  insertion_index = 0
  while insertion_index < len(sorted_list) and element >= sorted_list[insertion_index]:
    insertion_index += 1
  sorted_list.insert(insertion_index, element)
print(f"Sorted tuple: {tuple(sorted_list)}")
