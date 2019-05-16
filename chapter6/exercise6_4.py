def is_power(a, b):
	if a == 1:	#1 is power to the 0 for every number
		return True
	else:
		return a % b == 0 and is_power(a / b, b)
	return None


msg = 'Give numbers a and b, each followed by the enter key\n'
a = input(msg)
b = input()
print(is_power(a, b))
