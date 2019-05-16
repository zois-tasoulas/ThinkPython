def first(word):
	return word[0]

def last(word):
	return word[-1]

def middle(word):
	return word[1:-1]

def is_palindrome(word):
	if len(word) == 0 or len(word) == 1: 
		return True
	elif len(word) == 2:
		return first(word) == last(word)
	else:
		return first(word) == last(word) and is_palindrome(middle(word))
	return None

msg = 'Give a string to check if it is a palindrome:\n'
string = input(msg)
print(is_palindrome(string))
