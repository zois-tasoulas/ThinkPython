def chop(t):
	del t[0]
	del t[len(t) - 1]

lst = [10, 1, 57, 3, 82, 7, 28, 42, 243]
chop(lst)
print(lst)
