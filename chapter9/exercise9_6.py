def abecedarian(str1):
	ltr = 'a'
	for letter in str1:
		if ord(letter) < ord(ltr):
			return False
		ltr = letter
	return True

fin = open('words.txt')
count = 0
for line in fin:
	word = line.strip()
	if abecedarian(word):
		#print(word)
		count += 1
print("The number of abecedarian words is:", count, "\n")
