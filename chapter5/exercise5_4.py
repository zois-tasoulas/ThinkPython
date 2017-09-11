def recurse(n, s):
"""n should be an integer greater or equal to 0.
s can be a floating point number.
Provided that n >= 0, this function prints number B.
B = A + s
A = 1 + 2 + 3 + ... + n-1 + n
"""
	if n == 0:
		print(s)
	else:
		recurse(n-1, n+s)

recurse(3, 0)
