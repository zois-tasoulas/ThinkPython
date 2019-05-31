'''
build_list1 is significantly faster than build_list2.
t = t + [word] creates a new list in each iteration of the for loop.
This does not happend with append.

Creating a new list is time consuming as space has to be allocated and elements need to be copied.
'''

def build_list1():
	fin = open('../chapter9/words.txt')
	t = []
	for line in fin:
		word = line.strip()
		t.append(word)

def build_list2():
	fin = open('../chapter9/words.txt')
	t = []
	for line in fin:
		word = line.strip()
		t = t + [word]

build_list1()
build_list2()
