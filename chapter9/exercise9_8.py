def convert(num):
	if num < 10:
		return '00000' + str(num)
	elif num < 100:
		return '0000' + str(num)
	elif num < 1000:
		return '000' + str(num)
	elif num < 10000:
		return '00' + str(num)
	elif num < 100000:
		return '0' + str(num)
	else:	
		return str(num)

def ispalindrome(word):
	return word == word[::-1]

def satisfy(str1):
	if ispalindrome(str1[2:6]): 
		num = int(str1) + 1
		str1 = convert(num)
		if ispalindrome(str1[1:6]):
			num = int(str1) + 1
			str1 = convert(num)
			if ispalindrome(str1[1:5]):
				num = int(str1) + 1
				str1 = convert(num)
				if ispalindrome(str1):
					return True
	else:
		return False

count = 0
for num in range(0, 999996):
	string = convert(num)
	if satisfy(string):
		print(string)
		count += 1
print("The numbers that satisfy the requirements are:", count, "\n")
