def is_sorted(t):
	num1 = t[0]
	for num2 in t[1:]:
		if num1 > num2:
			return False
		num1 = num2
	return True

lst = [57, 56, 24, 24, 18, 42, 243]
print(is_sorted(lst))
lst = [10, 57, 82, 243, 243, 564]
print(is_sorted(lst))
lst = ['a', 'k', 'x', 'z']
print(is_sorted(lst))
