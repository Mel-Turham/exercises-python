user_sentences = input('Enter a sentence : ')
user_occurrences = input('Enter one occurrence : ')

def number_of_occurrences_in_sentence(sentences, occurrence):
  count = 0
  
  for i in sentences.lower():
    if i == occurrence.lower():
      count += 1
  return count

result = number_of_occurrences_in_sentence(user_sentences, user_occurrences)
print(result)
  
  

