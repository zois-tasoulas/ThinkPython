'''
Function read_dictionary is copied from:
http://greenteapress.com/thinkpython2/code/pronounce.py

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
'''

def read_dictionary(filename='c06d.txt'):
    """Reads from a file and builds a dictionary that maps from
    each word to a string that describes its primary pronunciation.

    Secondary pronunciations are added to the dictionary with
    a number, in parentheses, at the end of the key, so the
    key for the second pronunciation of "abdominal" is "abdominal(2)".

    filename: string
    returns: map from string to pronunciation
    """
    d = dict()
    fin = open(filename)
    for line in fin:

        # skip over the comments
        if line[0] == '#': continue

        t = line.split()
        word = t[0].lower()
        pron = ' '.join(t[1:])
        d[word] = pron

    return d

def puzzle_solver(d1, d2):
	lst = []
	for key in d1:
		if len(key) == 5:
			string1 = key[1:]
			string2 = key[0] + key[2:]
			if (key in d2) and (string1 in d2) and (string2 in d2):
				if d2[key] == d2[string1] and d2[key] == d2[string2]:
					lst.append(key)
	return lst

def build_dict():
	fin = open('../chapter9/words.txt')
	t = dict()
	for line in fin:
		word = line.strip()
		t[word] = 0
	return t

print("The words that solve the puzzle are:")
print(puzzle_solver(build_dict(), read_dictionary()))
