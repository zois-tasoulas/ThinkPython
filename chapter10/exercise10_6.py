def is_anagram(str1, str2):
	if len(str1) != len(str2):
		return False
	if sorted(str1) == sorted(str2):
		return True
	else:
		return False

word1 = input('Input the first string:\n')
word2 = input('Input the second string:\n')
print(is_anagram(word1, word2))
