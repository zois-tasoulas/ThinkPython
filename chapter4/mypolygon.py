import turtle
import math

def square(t, length):
	for i in range(4):
		t.fd(length)
		t.lt(90)
	print(t)
	turtle.mainloop()
	
def polygon(t, length, n):
	for i in range(n):
		t.fd(length)
		t.lt(360/n)
	print(t)
	turtle.mainloop()
	
def circle(t, r):
	sides = 200	#approximation of circle
	circ = 2 * math.pi * r
	leng = circ / sides
	polygon(t, leng, sides)
	
def arc(t, r, angle):
	sides = 200	#approximation of circle
	circ = 2 * math.pi * r
	leng = circ / sides
	arc_sides = sides * angle / 360
	int_arc_sides = int(arc_sides)
	for i in range(int_arc_sides):
		t.fd(leng)
		t.lt(360/sides)
	print(t)
	turtle.mainloop()
	
bob = turtle.Turtle()
#square(bob, 100)
#polygon(bob, 80, 3)
#circle(bob, 50)
arc(bob, 50, 180)
