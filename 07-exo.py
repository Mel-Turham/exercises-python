def join_word_with_underscore(words):
  word_split = words.split()
  result = '-'.join(word_split)
  return result
user_input = input('Enter a sentence: ') 
result = join_word_with_underscore(user_input)
print(result)