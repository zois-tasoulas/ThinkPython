import math

def mysqrt(a):
	e = 0.0000001
	if a != 1:
		x = a - 1.0
	else:
		x = 1.0
	while True:
		#print(x)
		y = (x + a / x) / 2
		if abs(y-x) < e:
			return y
		x = y

def test_square_root():
	print('a\tmysqrt(a)\tmath.sqrt(a)\tdiff')
	print('-\t---------\t------------\t----')
	for i in range(1, 10):
		a = mysqrt(i)
		b = math.sqrt(i)
		print (i, "\t", a, "\t", b,"\t", abs(a - b))

test_square_root()
#a = input('Give a number to find each square root:\n')
#print('The square root of the given number is:')
#print(mysqrt(a))
