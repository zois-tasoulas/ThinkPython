import turtle

def koch(t, length):
	if length < 3:
		t.fd(length)
	else:
		angle = 60
		koch(t, length // 3)
		t.lt(angle)
		koch(t, length // 3)
		t.rt(2*angle)
		koch(t, length // 3)
		t.lt(angle)
		koch(t, length // 3)

def snowflake(t, x):
	koch(t, x)
	t.rt(120)
	koch(t, x)
	t.rt(120)
	koch(t, x)

bob = turtle.Turtle()
#koch(bob, 200)
snowflake(bob, 200)
bob.hideturtle()
turtle.mainloop()
