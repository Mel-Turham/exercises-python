def elements_lists(list_elements, element):
	for item in list_elements:
		if element == item:
			list_elements.remove(element)

	return list_elements


list_numbers = [1, 3, 3, 5]

result = elements_lists(list_numbers, 5)

print(result)
