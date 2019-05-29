def consecutive3(str1):
	i = 0
	while i < len(str1) - 5:
		if (str1[i] == str1[i + 1]) and (str1[i + 2] == str1[i + 3]) and (str1[i + 4] == str1[i + 5]):
				return True
		i = i + 1
	return False

fin = open('words.txt')
count = 0
for line in fin:
	word = line.strip()
	if consecutive3(word):
		print(word)
		count += 1
print("The number of words with three consecutive letters is:", count, "\n")
