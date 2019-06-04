def build_list1():
	fin = open('../chapter9/words.txt')
	t = dict()
	i = 0
	for line in fin:
		word = line.strip()
		t[word] = i
		i += 1
	return t

d = build_list1()
print("zombie" in d)
print("Walmart" in d)
