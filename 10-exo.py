def is_lower_or_isLower(string):
  list_upper = ''.join([char for char in string if char.isupper()])
  list_lower = ''.join([char for char in string if char.islower()])
  result = list_lower + ' ' +  list_upper
  return result
  
  

user_input = input('Enter a string : ')

result = is_lower_or_isLower(user_input)
print(result)

