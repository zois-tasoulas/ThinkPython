#Is it 'aeirs'?

def avoids(str1, str2):
	for letter in str1:
		for lttr in str2:
			if letter == lttr:
				return False
	return True

fin = open('words.txt')
count = 0
strng = input('Input a string of forbidden letters:\n')
for line in fin:
	word = line.strip()
	if avoids(word, strng):
		count += 1
print("The number of words that don't contain", strng, "is", count, "\n")
