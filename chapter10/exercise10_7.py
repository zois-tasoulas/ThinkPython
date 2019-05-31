def has_duplicates(lst):
	t = lst
	t.sort()
	prev_elem = t[0]
	for elem in t[1:]:
		if elem == prev_elem:
			return False
		prev_elem = elem
	return True

mylist = [5, 2, 40, 67, 34, 4, 78]
print(has_duplicates(mylist))
