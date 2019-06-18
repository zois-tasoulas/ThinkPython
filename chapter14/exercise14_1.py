def sed(pat, rep, file1, file2):
	try:
		fd1 = open(file1, 'r')
	except:
		print('Error at opening first file')
		return
	try:
		fd2 = open(file2, 'w')
	except:
		print('Error at opening second file')
		return
	lst = []
	try:
		for line in fd1:
			lst = line.split()
			for i in range(len(lst)):
				if lst[i] == pat:
					fd2.write(rep)
				else:
					fd2.write(lst[i])
				if i != (len(lst) - 1):
					fd2.write(' ')
			fd2.write('\n')
	except:
		print('Error at reading or writing files')
		return
	try:
		fd1.close()
	except:
		print('Error at closing first file')
		return
	try:
		fd2.close()
	except:
		print('Error at closing second file')
		return

if __name__ == '__main__':
	sed('in', 'YOLO', 'in.txt', 'out.txt')
