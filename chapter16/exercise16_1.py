def time_to_int(time):
	return time.hour * 3600 + time.minute * 60 + time.second

def int_to_time(num):
	t = Time()
	(minutes, t.second) = divmod(num, 60)
	(t.hour, t.minute) = divmod(minutes, 60)
	return t

def mul_time(time, num):
	num2 = time_to_int(time)
	return int_to_time(num2 * num)

def pace(time, num):
	return mul_time(time, 1 / num)

if __name__ == '__main__':
	class Time:
		"""Represents the time of day.

		attributes: hour, minute, second
		"""
	t1 = Time()
	t1.hour = 0
	t1.minute = 46
	t1.second = 15
	t2 = pace(t1, 10)
	print("Pace is: %.2d:%.2d:%.2d" % (t2.hour, t2.minute, t2.second))
