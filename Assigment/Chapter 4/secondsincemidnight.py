def seconds_since_midnight(hour, minute, seconds):
			hour_in_seconds = hour * 3600
			minute_in_seconds = minute * 60
			time = hour_in_seconds + minute_in_seconds + seconds
			return (time)

hour = int (input('Enter hour: '))
minute = int (input('Enter minute: '))
seconds = int (input('Enter seconds: '))
print(hour,':',minute,':',seconds)
time = seconds_since_midnight(hour, minute, seconds)
print()
print(time)