from typing import List


def multiple_two_lists(list_1, list_2):
	product_list = []

	for item in range(len(list_1)):

		if len(list_1) > len(list_2):
			print(f'the length of {list_1} was be equal to a {list_2}')
		else:
			product_list.append(list_1[item] * list_2[item])

	return product_list


a = [1, 2, 3]

b = [4, 5, 6]

result = multiple_two_lists(a, b)

print(result)
