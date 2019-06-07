def anagrams(lst):
	d = dict()
	for word in lst:
		lst2 = []
		for letter in word:
			lst2.append(letter)
		lst2.sort()
		t = tuple(lst2)
		if t in d:
			d[t].append(word)
		else:
			d[t] = [word]
	return d

def print_anagrams(d):
	lst2 = []
	for key in d:
		if len(d[key]) > 1:
			lst2.append((len(d[key]), d[key]))
	lst2.sort(reverse=True)
	for (lngth, words) in lst2:
		print(words)

def print_scrabble_bingo(d):
	lst2 = []
	for key in d:
		if (len(key) == 8) and (len(d[key]) > 1):
			lst2.append((len(d[key]), key))
	lst2.sort(reverse=True)
	(i, b) = lst2[0]
	print("The collection(s) of 8 letters that forms the most possible bingos is(are):")
	for (num, key) in lst2:
		if num < i:
			break
		print(key)

def build_list1():
	fin = open('../chapter9/words.txt')
	t = []
	for line in fin:
		word = line.strip()
		t.append(word)
	return t

lst = build_list1()
d = anagrams(lst)
print_anagrams(d)
print_scrabble_bingo(d)
