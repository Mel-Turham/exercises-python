a = [2, 3, 9, 9, 9, 2, 3, 7, 8, 8, 10, 6]
 
new_list = []

for i in a:
  if i not in new_list:
    new_list.append(i)

list_sorted = sorted(new_list, reverse=False)
print(list_sorted)