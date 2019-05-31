def in_bisect(lst, val):
	leng = len(lst)
	mid = int(leng / 2)
	if leng == 0:
		return False
	elif leng == 1:
		return (lst[0] == val)
	elif leng == 2:
		return (lst[0] == val) or (lst[1] == val)
	elif val == lst[mid]:
		return True
	else:
		return in_bisect(lst[0: mid], val) or in_bisect(lst[(mid + 1):], val)

def reverse(strn):
	return strn[::-1]

def find_reverse(t):
	for i in range(len(t)):
		word = t.pop(0)
		if in_bisect(t, reverse(word)):
			print(word, reverse(word))

def build_list1():
	fin = open('../chapter9/words.txt')
	t = []
	for line in fin:
		word = line.strip()
		t.append(word)
	return t

lst = build_list1()
print("The words that have reverse pairs are:\n")
find_reverse(lst)
