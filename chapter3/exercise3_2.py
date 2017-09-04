def do_twice(f, val):
	f(val)
	f(val)

def print_twice(bruce):
	print(bruce)
	print(bruce)

def print_spam():
	print('spam')

def do_four(f,val):
	do_twice(f, val)
	do_twice(f, val)

do_four(print_twice, 'spam')
