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

def metathesis(d):
	for key in d:
		num = len(d[key])
		if num > 1:
			lst2 = d[key]
			for word1 in d[key]:
				del lst2[0]
				for word2 in lst2:
					displace = 0
					for i in range(len(word1)):
						if word1[i] != word2[i]:
							displace += 1
						if displace > 2:
							break
					if displace == 2:
						print(word1, word2)
				
def build_list1():
	fin = open('../chapter9/words.txt')
	t = []
	for line in fin:
		word = line.strip()
		t.append(word)
	return t

lst = build_list1()
d = anagrams(lst)
metathesis(d)
