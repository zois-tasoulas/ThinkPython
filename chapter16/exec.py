def print_time(time):
	print('%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))

def is_after(tm1, tm2):
	return (tm1.hour * 3600 + tm1.minute * 60 + tm1.second) > (tm2.hour * 3600 + tm2.minute * 60 + tm2.second)

def increment(time, seconds):
	newt = Time()

	newt.second = time.second + seconds
	newt.minute = time.minute
	newt.hour = time.hour
	if newt.second >= 60:
		newt.minute += newt.second / 60
		newt.second = newt.second % 60
	if newt.minute >= 60:
		newt.hour += newt.minute / 60
		newt.minute = newt.minute % 60
	return newt

if __name__ == '__main__':
	class Time:
		"""Represents the time of day.
	
		attributes: hour, minute, second
		"""
	
	t1 = Time()
	t1.hour = 11
	t1.minute = 42
	t1.second = 35
	print_time(t1)
	t2 = Time()
	t2.hour = 11
	t2.minute = 42
	t2.second = 30
	print(is_after(t1, t2))
	print_time(increment(t1, 195))
