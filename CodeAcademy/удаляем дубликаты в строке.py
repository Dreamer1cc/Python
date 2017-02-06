def remove_duplicates(lst):
	new_list = []
	for i in lst:
		if i not in new_list:
			new_list.append(i)
	return new_list

remove_duplicates([1,1,2,2])