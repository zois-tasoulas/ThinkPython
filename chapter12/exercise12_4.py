reduc = dict({'' : 0})

def reducible(w, d):
	if w in reduc:
		return True
	else:
		for i in range(len(w)):
			lst2 = list(w)
			del lst2[i]
			word2 = ''
			for let in lst2:
				word2 = word2 + let
			if word2 in reduc:
				return True
			elif (word2 in d) and (reducible(word2, d)):
				reduc[word2] = 0
				return True
		return False

def find_longest(d):
	lst = []
	longest = 0
	long_words = []
	for key in d:
		if reducible(key, d):
			lst.append((len(key), key))
	for (num, word) in lst:
		print(word)
		if num > longest:
			longest = num
	for (num, word) in lst:
		if num == longest:
			long_words.append(word)
	print("The logest word(s) is(are):")
	for word in long_words:
		print(word)

def build_list1():
	fin = open('../chapter9/words.txt')
	t = dict()
	for line in fin:
		word = line.strip()
		t[word] = 0
	return t

d = build_list1()
#d ={"sprite" : 0, "spite" : 0, "spit" : 0, "pit" : 0, "it" : 0, "i" : 0}
find_longest(d)
