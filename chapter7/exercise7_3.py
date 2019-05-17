import math

def estimate_pi():
	mypi = 0
	cur_pi = 500
	k = 0 
	while cur_pi > 1e-15:
		cur_pi = (math.factorial(4 * k) * (1103 + 26390 * k)) / (pow(math.factorial(k), 4) * pow(396, 4 * k))
		mypi = mypi + cur_pi
		k = k + 1
	mypi = mypi * 2 * math.sqrt(2) / 9801
	return mypi


myval = estimate_pi()
print("My 1/pi is: ", myval)
print("The absolute difference with Python's 1/pi is: ", abs((1 / math.pi)) - myval)
