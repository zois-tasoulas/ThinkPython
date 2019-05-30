def nested_sum(t):
	mysum = 0
	for lst in t:
		for num in lst:
			mysum += num

	return mysum

lst = [[2], [2, 3], [15, 5, 10, 4], [5], [3, 1]]
print(nested_sum(lst))
