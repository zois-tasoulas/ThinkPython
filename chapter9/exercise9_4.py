def uses_only(str1, str2):
	flag = True
	for letter in str1:
		if flag == False:
			break
		flag = False
		for lttr in str2:
			if letter == lttr:
				flag = True
				break
	return flag

fin = open('words.txt')
strng = input('Input a letter list:\n')
for line in fin:
	word = line.strip()
	if uses_only(word, strng):
		print(word)
