import time

t = time.time()
days = t // (24 * 60 * 60)
remainder = t % (24 * 60 * 60)
hours = remainder // (60 * 60)
remainder = remainder % (60 * 60)
minutes = remainder // 60
seconds = remainder % 60
print('There have passed', int(days), 'days', int(hours), 'hours', int(minutes), 'minutes and', int(seconds), 'seconds since the epoch.')
