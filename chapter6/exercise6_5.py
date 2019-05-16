def gcd(a, b):
	if b == 0:
		return a
	else:
		return gcd(b, a % b)
	return None


msg = 'Give numbers a and b to find their greatest common divisor, each followed by the enter key\n'
a = input(msg)
b = input()
print(gcd(a, b))
