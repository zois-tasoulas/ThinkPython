import os
import sys

def search(direct):
	lst = []
	for obj in os.listdir(direct):
		path = os.path.join(direct, obj)
		if os.path.isfile(path):
			(name, ext) = os.path.splitext(path)
			if ext == '.mp3':
				lst.append(path)
		elif os.path.isdir(path):
			lst += search(path)
	return lst

def find_duplicates(lst):
	drct = dict()
	words = []
	for mmbr in lst:
		member = mmbr.replace(" ", "\ ")
		cmd1 = 'md5sum ' + member
		fp = os.popen(cmd1)
		res = fp.read()
		words = res.split()
		if words[0] in drct:
			cmd2 = 'diff ' + member + ' ' + drct[words[0]]
			fp = os.popen(cmd2)
			res2 = fp.read()
			if res2 == '':
				print('Files %s and %s are duplicates' % (member, drct[words[0]]))
		else:
			drct[words[0]] = member

if __name__ == '__main__':
	if len(sys.argv) == 2:
		direct = sys.argv[1]
	else:
		direct = os.getcwd()
	lst = search(direct)
	find_duplicates(lst)
