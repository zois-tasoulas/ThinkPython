def ack(m, n):
	if m < 0 or n < 0:
		print('m and n should be non negative integers')
		return None
	if m == 0:
		return n + 1
	if n == 0:
		return ack(m - 1, 1)
	else:
		return ack(m - 1,ack(m, n - 1))


msg = 'Give two integers, each followed by the enter key\n'
x = input(msg)
y = input()
print(ack(int(x), int(y)))
