import random
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

def bisect(lst, val, minim, maxim):
	leng = maxim - minim + 1
	mid = minim + int(leng / 2)
	if leng < 1:
		return (False, -5)
	elif leng == 1:
		return (lst[minim] >= val, minim)
	elif leng == 2:
		if lst[minim] >= val :
			return (True, minim) 
		else:
			return (lst[maxim] >= val, maxim)
	elif val == lst[mid]:
		return (True, mid)
	elif val < lst[mid]:
		return bisect(lst, val, minim, mid) 
	else:
		return bisect(lst, val, mid + 1, maxim)

def choose_from_hist(dic):
	lst1 = []
	lst2 = []
	mysum = 0
	for key in dic:
		lst1.append(key)
		mysum += dic[key]
		lst2.append(mysum)
	x = random.randint(1, mysum)
	(logic, y) = bisect(lst2, x, 0, len(lst2) - 1)
	if logic == True:
		return lst1[y]
	else:
		raise ValueError('Binary search returned false')

(dic, count) = read_file('book2.txt')
x = choose_from_hist(dic)
print(x)
