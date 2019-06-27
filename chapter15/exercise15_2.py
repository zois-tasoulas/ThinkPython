import turtle
import math
from exercise15_1 import Circle, Point, Rectangle

def draw_rect(t, rect):
	for i in range(2):
		t.fd(rect.width)
		t.lt(90)
		t.fd(rect.height)
		t.lt(90)
	print(t)
	turtle.mainloop()

def polygon(t, length, n):
	for i in range(n):
		t.fd(length)
		t.lt(360/n)
	print(t)
	turtle.mainloop()
	
def draw_circle(t, crcl):
	sides = 300	#approximation of circle
	circ = 2 * math.pi * crcl.radius
	leng = circ / sides
	polygon(t, leng, sides)

if __name__ == '__main__':
	bob = turtle.Turtle()
	rec = Rectangle()
	rec.width = 42
	rec.height = 59
	rec.corner = Point()
	rec.corner.x = 2
	rec.corner.y = 1
	cir = Circle()
	cir.center = Point()
	cir.center.x = 5
	cir.center.y = 7
	cir.radius = 83

	draw_rect(bob, rec)
	draw_circle(bob, cir)
