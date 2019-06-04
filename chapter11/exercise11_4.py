def has_duplicates(lst):
	d = dict()
	for elem in lst:
		if elem in d:
			return True
		else:
			d[elem] = 1
	return False

mylist = [5, 2, 40, 67, 34, 4, 78, 3, 42, 40]
print(has_duplicates(mylist))
