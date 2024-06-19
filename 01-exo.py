# Ask user to inter a number or ascii_letters

characters = input('Please make sure to type a letter or number : ')

# Verified if the character is in uppercase()
if characters.isupper():
  print(f'The letter {characters} is in uppercase')

# Verified if the character is a number
elif characters.isdigit():
  print(f'the characters {characters} is a number')
# Verified if the character is in lowercase()
elif characters.islower():
   print(f'The letter {characters} is in lowercase')
else:
  print(f'the characters {characters} is neither number or letter')
