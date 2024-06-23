def square_lists(lists):
	square_numbers = list(map(lambda x: x * x, lists))
	return square_numbers


items = [1, 2, 3, 4, 5, 6, 7]


result = square_lists(items)

print(result)

