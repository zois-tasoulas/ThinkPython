#This will return True for the first lower case character of s
def any_lowercase1(s):
	for c in s:
		if c.islower():
			return True
		else:
			return False

#This will alsways return True as islower() is invoked on the character 'c'
def any_lowercase2(s):
	for c in s:
		if 'c'.islower():
			return 'True'
		else:
			return 'False'

#This function will return True is the last character of the string is lower case, otherwise it will return false
def any_lowercase3(s):
	for c in s:
		flag = c.islower()
	return flag

#This function will return True if at least one character of s is lower case
def any_lowercase4(s):
	flag = False
	for c in s:
		flag = flag or c.islower()
	return flag

#This function will return True if all the characters of s are lower case
def any_lowercase5(s):
	for c in s:
		if not c.islower():
			return False
	return True
