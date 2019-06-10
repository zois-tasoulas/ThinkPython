import string

def read_file(f):
	fin = open(f)
	t = []
	for line in fin:
		words = line.strip()
		transtab = str.maketrans("", "", string.punctuation)
		words = words.translate(transtab)
		for word in words.split():
			t.append(word)
	return t
		

lst = read_file('file.txt')
for word in lst:
	print(word)
