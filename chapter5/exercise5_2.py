def check_fermat(a, b, c, n):
	x = a**n + b**n
	y = c**n
	if n > 2 and x == y:
		print("Holy smokes, Fermat was wrong!")
	else:
		print("No, that doesn't work")

def prompt():
	prompt_msg = 'Please provide four positive integers, a, b,c and n, each followed by enter key. n has to be grater than 2\n'
	a = input(prompt_msg)
	b = input()
	c = input()
	n = input()
	check_fermat(int(a), int(b), int(c), int(n))


prompt()
