#Question 1
r = 5
v = (4 * 3.14159 * r**3) /3	# V = (4*pi*r^3) / 3 
print('The volume of a sphere with radius 5 is: ')
print(v)

#Question 2
p = 24.95
d = 0.4
numofbooks = 60
c = numofbooks * p * (1 - d) + 3 + 0.75 * (numofbooks - 1)
print('The total wholesale cost for 60 books is: ')
print(c, 'dollars')

#Question 3
easymiles = 2
easytempo = 495 	# in seconds
mediummiles = 3
mediumtempo = 432 	# in seconds

totaltime = easymiles * easytempo + mediummiles * mediumtempo # in seconds
totalmin = totaltime / 60	# in minutes
returnmin = totalmin - 8	# because I leave at 6:52
print('I return home at 7 and', returnmin, 'minutes')
