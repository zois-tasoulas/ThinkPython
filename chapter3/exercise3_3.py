def print_2x2grid():
	print_2row()
	print('+')
	do_four(print_2cell)
	print_2row()
	print('+')
	do_four(print_2cell)
	print_2row()
	print('+')

def print_4x4grid():
	print_4row()
	print('+')
	do_four(print_4cell)
	print_4row()
	print('+')
	do_four(print_4cell)
	print_4row()
	print('+')
	do_four(print_4cell)
	print_4row()
	print('+')
	do_four(print_4cell)
	print_4row()
	print('+')

def print_2row():
	print('+ ', end = '')
	print('- ' * 4, end = '')
	print('+ ', end='')
	print('- ' * 4, end = '')

def print_4row():
	do_twice(print_2row)

def print_2cell():
	print('| ', ' ' * 6, '| ', ' ' * 6, '|')

def print_4cell():
	print('| ', ' ' * 6, '| ', ' ' * 6, end = '')
	print(' | ', ' ' * 6, '| ', ' ' * 6, end = '')
	print(' |')

def do_twice(f):
	f()
	f()

def do_four(f):
	f()
	f()
	f()
	f()

print_2x2grid()
print()
print_4x4grid()
