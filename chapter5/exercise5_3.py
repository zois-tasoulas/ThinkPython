def is_triangle(a, b, c):
	if a > b + c or b > a + c or c > a + b:
		print('No')
	else:
		print('Yes')

def prompt():
	prompt_msg = 'Please provide three possible triangle side lengths, each followed by enter key.\n'
	a = input(prompt_msg)
	b = input()
	c = input()
	is_triangle(int(a), int(b), int(c))


prompt()
