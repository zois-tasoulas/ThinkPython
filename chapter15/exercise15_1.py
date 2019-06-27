class Point:
	"""Represents a 2D point.

	attributes: x, y.
	"""

class Circle:
	"""Represents a circle.

	attributes: center, radius.
	"""
class Rectangle:
	"""Represents a rectangle.
	The provided corner should be the one with the lowest x
	and y coordinates.

	attributes: width, height, corner.
	"""

def within_limits(a, b, c):
	return (a - b <= c <= a + b)

def point_in_circle(crcl, pnt):
		return within_limits(crcl.center.x, crcl.radius, pnt.x) and within_limits(crcl.center.y, crcl.radius, pnt.y)

def rect_in_circle(crcl, rec):
	(x1, y1) = (rec.corner.x, rec.corner.y)
	(x2, y2) = (rec.corner.x, rec.corner.y + rec.height)
	(x3, y3) = (rec.corner.x + rec.width, rec.corner.y)
	(x4, y4) = (rec.corner.x + rec.width, rec.corner.y + rec.height)
	a = within_limits(crcl.center.x, crcl.radius, x1) and within_limits(crcl.center.x, crcl.radius, y1)
	b = within_limits(crcl.center.x, crcl.radius, x2) and within_limits(crcl.center.x, crcl.radius, y2)
	c = within_limits(crcl.center.x, crcl.radius, x3) and within_limits(crcl.center.x, crcl.radius, y3)
	d = within_limits(crcl.center.x, crcl.radius, x4) and within_limits(crcl.center.x, crcl.radius, y4)
	return (a and b and c and d)

def rect_circle_overlap(crcl, rec):
	mypoint = Point()
	(x1, y1) = (rec.corner.x, rec.corner.y)
	(x2, y2) = (rec.corner.x, rec.corner.y + rec.height)
	(x3, y3) = (rec.corner.x + rec.width, rec.corner.y)
	(x4, y4) = (rec.corner.x + rec.width, rec.corner.y + rec.height)
	if rect_in_circle(crcl, rec):
		return True
	else:
		mypoint.x = x1
		for i in range(y1, y2 + 1):
			mypoint.y = i
			if point_in_circle(crcl, mypoint):
				return True
		mypoint.x = x3
		for i in range(y3, y4 + 1):
			mypoint.y = i
			if point_in_circle(crcl, mypoint):
				return True
		mypoint.y = y1
		for i in range(x1, x3 + 1):
			mypoint.x = i
			if point_in_circle(crcl, mypoint):
				return True
		mypoint.y = y3
		for i in range(x2, x4 + 1):
			mypoint.x = i
			if point_in_circle(crcl, mypoint):
				return True
	return False

if __name__ == '__main__':
	mycircle = Circle()
	mycircle.center = Point()
	mycircle.center.x = 150
	mycircle.center.y = 100
	mycircle.radius = 75
	mypoint = Point()
	mypoint.x = 100
	mypoint.y = 25
	myrec = Rectangle()
	myrec.width = 100
	myrec.height = 20
	myrec.corner = Point()
	myrec.corner.x = 100
	myrec.corner.y = 15
	print(point_in_circle(mycircle, mypoint))
	print(rect_in_circle(mycircle, myrec))
	print(rect_circle_overlap(mycircle, myrec))
