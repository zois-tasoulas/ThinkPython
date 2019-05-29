def uses_all(str1, str2):
	flag = True
	for letter in str2:
		if flag == False:
			break
		flag = False
		for lttr in str1:
			if letter == lttr:
				flag = True
				break
	return flag

fin = open('words.txt')
count = 0
strng = input('Input a letter list:\n')
for line in fin:
	word = line.strip()
	if uses_all(word, strng):
		print(word)
		count += 1
print("The number of words that use all", strng, "at least ones, is:", count, "\n")
