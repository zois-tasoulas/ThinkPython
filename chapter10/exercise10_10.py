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

def build_list1():
	fin = open('../chapter9/words.txt')
	t = []
	for line in fin:
		word = line.strip()
		t.append(word)
	return t

elem = input('Input a word to search the file:\n')
print(in_bisect(build_list1(), elem))
