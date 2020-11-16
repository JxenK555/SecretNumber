import random
first = input('Please Insert Your Smallest Number: ')
last = input('Please Insert Your Biggest Number: ')
first = int(first)
last = int(last)

r = random.randint(first, last)
turn = 0
while True:
	turn += 1
	number = input('Try A Number: ')
	number = int(number)
	if number == r:
		print('You Are Right')
		print('You Have Use', turn, "Time")
		break
	elif number > r:
		print('Sorry, Try A Smaller Number')
	elif number < r:
		print('Sorry, Try A Bigger Number')