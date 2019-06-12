import random
import string

def markov_analys(f, leng=2):
	fin = open(f)
	t = dict()
	space = " "
	suffix = ""
	for line in fin:
		words = line.strip()
		lst = words.split()
		for word in lst:
			lst2 = suffix.split()
			if len(lst2) == leng:
				if suffix in t:
					if word not in t[suffix]:
						t[suffix].append(word)
				else:
					t[suffix] = [word]
				suffix = space.join(lst2[1:]) + space + word
			elif len(lst2) > leng:
				raise ValueError('Suffix longer than leng')
			else:
				suffix = suffix + space + word
	return t

def random_text(d):
	key = random.choice(list(d.keys()))
	space = " "
	word = random.choice(d[key])
	while not word[0].isupper():
		key = random.choice(list(d.keys()))
		word = random.choice(d[key])
	text = word
	key = random.choice(list(d.keys()))
	for i in range(35):
		word = random.choice(d[key])
		text = text + space + word
		lst2 = key.split()
		key = space.join(lst2[1:]) + space + word
	while (text[-1] != '.') and (text[-1] != '!') and (text[-1] != '?'):
		word = random.choice(d[key])
		text = text + space + word
		lst2 = key.split()
		key = space.join(lst2[1:]) + space + word
	return text

dic = markov_analys('book3.txt', 3)
print(random_text(dic))
