def is_palidrome(word):
	return word == word[::-1]

print(is_palidrome(input("Give a string to check if it is a palindrome:\n")))
