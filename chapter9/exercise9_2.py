def has_no_e(strn):
	for letter in strn:
		if letter == 'e':
			return False
	return True

fin = open('words.txt')
count = 0
tot = 0
for line in fin:
	tot += 1
	word = line.strip()
	if has_no_e(word):
		print(word)
		count += 1
print("The percentage of words without 'e' is, ", (count * 100 / tot),"%\n")
