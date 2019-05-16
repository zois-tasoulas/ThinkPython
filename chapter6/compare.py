def compare(x, y):
	if x > y:
		return 1
	elif x == y:
		return 0
	else:
		return -1

msg = 'Provide two numbers, each followed by the enter key.\n'
a = input(msg)
b = input()
c = compare(int(a), int(b))
print(c)
