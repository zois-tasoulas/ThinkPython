def in_bisect(lst, val, minim, maxim):
	leng = maxim - minim + 1
	mid = minim + int(leng / 2)
	if leng == 0:
		return (False, None)
	elif leng == 1:
		if lst[minim] == val:
			return (True, minim)
		else:
			return (False, None)
	elif leng == 2:
		if lst[minim] == val:
			return (True, minim)
		elif lst[maxim] == val:
			return (True, maxim)
		else:
			return (False, None)
	elif val == lst[mid]:
		return (True, mid)
	elif val < lst[mid]:
		return in_bisect(lst, val, minim, mid - 1)
	else:
		return in_bisect(lst, val, mid + 1, maxim)

def build_list1():
	fin = open('../chapter9/words.txt')
	t = []
	for line in fin:
		word = line.strip()
		t.append(word)
	return t

elem = input('Input a word to search the file:\n')
lst = build_list1()
(logic, val) = in_bisect(lst, elem, 0, len(lst) - 1)
print(val)
