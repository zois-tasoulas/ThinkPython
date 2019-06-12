import string
import matplotlib.pyplot as plt
from math import log

def read_file(f):
	header = True
	fin = open(f)
	t = dict()
	count = 0
	spaces = ""
	for char in string.punctuation:
		spaces = spaces + " "
	for line in fin:
		words = line.strip()
		if (words == "CHAPTER I.") or (words == "Chapter 1") or (words == "CHAPTER I"):
			header = False
		if header == False:
			transtab = str.maketrans(string.punctuation, spaces)
			transtab2 = str.maketrans("“”", "  " )
			words = words.translate(transtab)
			words = words.translate(transtab2)
			words = words.lower()
			lst = words.split()
			if (len(lst) > 6) and (lst[4] =="gutenberg") and (lst[5] == "ebook"):
				break
			if (lst != []) and (lst[0] != "chapter"):
				for word in lst:
					if (len(word) > 1) or (word == 'i') or (word == 'a'):
					
						t[word] = t.get(word, 0) + 1
	return t

def print_list(d):
	lst = []
	lst2 = []
	r = 0
	for key in d:
		lst.append((d[key], key))
	lst.sort(reverse=True)
	for (freq, word) in lst:
		r += 1
		lst2.append((r, freq))
		print(r, freq)
	return lst2

def plot_line(lst):
	lst2 = [(log(x), log(y)) for (x, y) in lst]
	(w, z) = zip(*lst2)
	plt.plot(w, z)
	plt.xlabel('log of rank')
	plt.ylabel('lof of frequency')
	plt.show()

dic = read_file('book3.txt')
lst = print_list(dic)
plot_line(lst)
