

def join_two_list(list_1, list_2):
  full_list = []
  for i in list_1:
    print(i)
    if i in list_2:
     list_2.remove(i)
    else:
      full_list.append(i)
  return full_list
first_list = [1, 2, 3, 4, 5]
second_list = [4, 5, 6, 7, 8]

result = join_two_list(first_list, second_list)

print(result)