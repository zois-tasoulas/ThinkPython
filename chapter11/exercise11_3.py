known = dict()

def ack(m, n):
	if m < 0 or n < 0:
		print('m and n should be non negative integers')
		return None
	if (m, n) in known:
		return known[(m, n)]
	elif m == 0:
		known[(m, n)] = n + 1
		return n + 1
	elif n == 0:
		known[(m, n)] = ack(m - 1, 1)
		return known[(m, n)]
	else:
		known[(m, n)] = ack(m - 1, ack(m, n - 1))
		return known[(m, n)]


msg = 'Give two integers, each followed by the enter key\n'
x = input(msg)
y = input()
print(ack(int(x), int(y)))
