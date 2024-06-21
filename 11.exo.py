def unique_characters(string):
  unique_character_in_string = []
  for character in string:
    if character not in unique_character_in_string:
      unique_character_in_string.append(character)
    else:
      unique_character_in_string.remove(character)
      
  return len(unique_character_in_string)

input_string = input("Enter a string: ")

result = unique_characters(input_string)

print(result)


 