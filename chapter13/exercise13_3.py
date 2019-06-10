import string

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
					
						if word in t:
							t[word] += 1
						else:
							t[word] = 1
							count += 1
	return (t, count)

#This function can also be done with complexity O(n)
def print_20_freq(d):
	lst = []
	for word in d:
		lst.append((d[word], word))
	lst.sort(reverse=True)
	print("The 20 most frequent words are:")
	for i in range(20):
		(num, word) = lst[i]
		print(word)

(dic, count) = read_file('book.txt')
print("In the book, the words that appear in total are:")
print(count)
print_20_freq(dic)
