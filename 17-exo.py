def palindrome(string):
	string = string.lower()
	string = ''.join(e for e in string if e.isalnum())

	return string == string[::-1]


user_input = input('Enter a word : ')

if palindrome(user_input):
	print(f'{user_input} is a palindrome')
else:
	print(f'{user_input} is not a palindrome')


