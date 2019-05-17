def eval_loop():
	old_string = ''
	while True:
		string = input('Give an expression to evaluate, or type done to exit:\n')
		if string == 'done':
			print(old_string)
			break
		else:
			old_string = eval(string)
			print(old_string)

eval_loop()
