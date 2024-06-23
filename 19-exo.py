import math
import random


def random_number_in_list(lists: list):
	new_list = []
	for number in lists:
		if new_list.count(number) == 1:
			new_list.append(random.randrange(lists[0], lists[-1]))

	return new_list


items_list = [1, 2, 3, 4, 5, 6, 7]

result = random_number_in_list(items_list)

print(result)
