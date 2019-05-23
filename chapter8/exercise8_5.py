def rotate_word(stn, num):
	new_str = ""
	for letter in stn:
		new_let = chr(ord(letter) + num)
		new_str = new_str + new_let
	return new_str

s = input('Give a string to encrypt:\n')
n = input('Give the number of rotations for the code:\n')
print(rotate_word(s, int(n)))
