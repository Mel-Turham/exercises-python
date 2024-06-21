
def somme_two_list(list_1, list_2):
  list_3 = []
  
  for i in range(len(list_1)):
    if len(list_2) < len(list_1):
      print(f'Operation not possible ')
    else:
      result = list_1[i] + list_2[i]
      list_3.append(result)
      
  return list_3

first_list = [1,2,3]
second_list = [4,5,6]

print(somme_two_list(first_list, second_list))