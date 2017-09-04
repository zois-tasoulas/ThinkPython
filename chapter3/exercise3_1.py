def right_justify(s):
	x = len(s)
	y = ' '*(70 - x)
	print(y+s)

right_justify('Learning Python')
