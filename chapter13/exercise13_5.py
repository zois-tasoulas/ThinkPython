import random

def choose_from_hist(t):
	tot = 0
	lst = []
	for mem in t:
		tot += t[mem]
		for i in range(t[mem]):
			lst.append(mem)
	return lst[random.randint(0, (tot - 1))]

def histogram(t):
	d = dict()
	for mem in t:
		d[mem] = d.get(mem, 0) + 1
	return d

t = ['a', 'b', 'a', 'c', 'b']
x = choose_from_hist(histogram(t))
print(x)
