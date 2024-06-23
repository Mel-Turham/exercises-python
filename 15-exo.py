def join_tow_list(list_1, list_2):
	two_lists = []
	filter_list_1 = list(set(list_1))
	filter_list_2 = list(set(list_2))

	full_list = filter_list_1 + filter_list_2
	for item in full_list:
		if item not in two_lists:
			two_lists.append(item)

	return two_lists


result = join_tow_list([1, 1, 3, 4], [3, 3, 4, 5])

print(result)

