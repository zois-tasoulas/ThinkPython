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

def first(strn):
	word = []
	i = 0
	for let in strn:
		if (i % 2) == 0:
			word.append(let)
		i += 1
	return ''.join(word)

def second(strn):
	word = []
	i = 0
	for let in strn:
		if (i % 2) == 1:
			word.append(let)
		i += 1
	return ''.join(word)

def w3_first(strn):
	word = []
	i = 0
	for let in strn:
		if (i % 3) == 0:
			word.append(let)
		i += 1
	return ''.join(word)

def w3_second(strn):
	word = []
	i = 0
	for let in strn:
		if (i % 3) == 1:
			word.append(let)
		i += 1
	return ''.join(word)

def w3_third(strn):
	word = []
	i = 0
	for let in strn:
		if (i % 3) == 2:
			word.append(let)
		i += 1
	return ''.join(word)

def find_interlock(t):
	for word in t:
		if in_bisect(t, first(word)):
			if in_bisect(t, second(word)):
				print(word, first(word), second(word))

def find_threew_interlock(t):
	for word in t:
		if in_bisect(t, w3_first(word)):
			if in_bisect(t, w3_second(word)):
				if in_bisect(t, w3_third(word)):
					print(word, w3_first(word), w3_second(word), w3_third(word))

def build_list1():
	fin = open('../chapter9/words.txt')
	t = []
	for line in fin:
		word = line.strip()
		t.append(word)
	return t

lst = build_list1()
print("The pairs that form interlocks are:\n")
find_interlock(lst)
print("The triplets that form three-way interlocks are:\n")
find_threew_interlock(lst)
