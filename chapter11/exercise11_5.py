'''
Works for words with lower case letters only
'''

def rotate_pairs(d):
	for key in d:
		for num in range(1, 26):
			new_str = ""
			for letter in key:
				if (ord(letter) + num) > ord('z'):
					let = ord('a') - 1 + (ord(letter) + num - ord('z'))
				else:
					let = ord(letter) + num
				new_let = chr(let)
				new_str = new_str + new_let
			if new_str in d:
				d[key].append(new_str)
	return d

def build_list1():
	fin = open('../chapter9/words.txt')
	d = dict()
	for line in fin:
		word = line.strip()
		d[word] = []
	return d

print("The rotate pairs are:")
d = rotate_pairs(build_list1())
for key in d:
	if d[key] != []:
		print(key, d[key])
