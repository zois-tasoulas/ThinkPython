import math

def hypotenuse(x, y):
	return math.sqrt(x**2 + y**2)

msg = 'Give the lengths of the two sides of a right triangle each followed by the enter key\n'
a = input(msg)
b = input()
c = hypotenuse(int(a), int(b))
print('The length of the hypotenuse is', c)
