def remove_vowels(string):
  vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
  return ''.join([char for char in string if char not in vowels])


string = 'Hello, world'

result = remove_vowels(string)

print(result)