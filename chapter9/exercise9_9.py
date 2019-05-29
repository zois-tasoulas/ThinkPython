def reverse(num1, num2):
	strng = str(num1)
	str1 = strng.zfill(2) 
	strng = str(num2)
	str2 = strng.zfill(2) 
	if (str1[0] == str2[1]) and (str1[1] == str2[0]):
		return True
	else:
		return False

#Assuming a girl younger than 10 cannot have a child
for num in range(10, 99):
	count = 0
	for i in range(1, 89):
		if (i + num) > 99:
			break
		if reverse(i, i + num):
			count += 1
			if count == 6:
				age = i	
			if count == 8:
				print("My age is", age,"\n")
