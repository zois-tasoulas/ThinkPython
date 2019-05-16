def is_between(x, y, z):
	return x <= y <= z

msg = 'Give three numbers, each followed by enter key\n'
x = input(msg)
y = input()
z = input()
print(is_between(int(x), int(y), int(z)))
