def cumsum(t):
	mysum = 0
	for i in range(len(t)):
		t[i] += mysum
		mysum = t[i]

	return t

lst = [10, 1, 5, 3, 2, 7, 28]
print(cumsum(lst))
