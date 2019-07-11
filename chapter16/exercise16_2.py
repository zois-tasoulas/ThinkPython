from datetime import datetime, timedelta
from calendar import monthrange

def print_day():
	today = datetime.today()
	print("Today is %s\n" % today.strftime('%A'))

def next_bday(birthday):
	today = datetime.today()
	print("The users age is %d\n" % (today.year - birthday.year))

	seconds = 0
	minutes = 0
	hours = 0
	days = 0
	months = 0
	seconds = birthday.second - today.second
	if seconds < 0:
		seconds += 60
		minutes = -1
	minutes += birthday.minute - today.minute
	if minutes < 0:
		minutes += 60
		hours = -1
	hours += birthday.hour - today.hour
	if hours < 0:
		hours += 24
		days = -1
	days += birthday.day - today.day
	if days < 0:
		(first, ds) = monthrange(today.year, today.month)
		days += ds
		months -= 1
	months += birthday.month - today.month
	if months < 0:
		months = months + 12
	print("Next birthday will be in %d months, %d days, %d hours, %d minutes and %d seconds\n" % (months, days, hours, minutes, seconds))

def double_day(bday1, bday2):
	'''
		Calculate double day for age in the granularity of days
	'''
	if bday1 == bday2:
		print("Double day is not possible, birthdays on the same date\n")
	elif bday1 > bday2:
		dif = (bday1 - bday2).days
		ddate = bday1 + timedelta(days=dif)
		print("The double date is %s (dd-mm-yyyy)\n" % ddate.strftime('%d-%m-%Y'))
	else:
		dif = (bday2 - bday1).days
		ddate = bday2 + timedelta(days=dif)
		print("The double date is %s (dd-mm-yyyy)\n" % ddate.strftime('%d-%m-%Y'))

def nth_day(bday1, bday2):
	'''
		Calculate nth day for age in the granularity of days
	'''
	n = int(input("How many times do you want the two ages to differ?\n"))
	if bday1 == bday2:
		print("%d th day is not possible, birthdays on the same date" % n)
	elif bday1 > bday2:
		dif = (bday1 - bday2).days
		ddate = bday1 + timedelta(days=((n - 1) * dif))
		print("The %d th date is %s (dd-mm-yyyy)" % (n, ddate.strftime('%d-%m-%Y')))
	else:
		dif = (bday2 - bday1).days
		ddate = bday2 + timedelta(days=((n - 1) * dif))
		print("The %d th date is %s (dd-mm-yyyy)" % (n, ddate.strftime('%d-%m-%Y')))

if __name__ == '__main__':
	print_day()
	bday = datetime(1944, 9, 14)
	next_bday(bday)
	bday2 = datetime(2004, 7, 11)
	double_day(bday, bday2)
	nth_day(bday, bday2)
