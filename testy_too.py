import random

number = random.randint(1,100)
game_on = True
previous_guess = 0

while game_on == True:
	guess_raw = raw_input("Guess a number between 1 and 100: ")
	current_guess = int(guess_raw)

	if current_guess == number:
		replay = raw_input("you guessed it! want to play again (y/n)?" )
		if replay == "y":
			number = random.randint(1,100)
			game_on = True
		else:
			print "cool. see you next time!"
			game_on = False
	elif abs(current_guess - number)<= 5:
		print "scalding"
		if previous_guess == 0:
			attempt = 1
		elif abs(current_guess-number) < abs(previous_guess-number):
			print "you're getting closer"
		elif abs(current_guess-number) > abs(previous_guess-number):
			print "you're getting further away"
		previous_guess = current_guess
	elif abs(current_guess - number) <= 10:
		print "hot"
		if previous_guess == 0:
			attempt = 1
		elif abs(current_guess-number) < abs(previous_guess-number):
			print "you're getting closer"
		elif abs(current_guess-number) > abs(previous_guess-number):
			print "you're getting further away"
		previous_guess = current_guess
	elif abs(current_guess-number) <=20:
		print "warm"
		if previous_guess == 0:
			attempt = 1
		elif abs(current_guess-number) < abs(previous_guess-number):
			print "you're getting closer"
		elif abs(current_guess-number) > abs(previous_guess-number):
			print "you're getting further away"
		previous_guess = current_guess
	elif abs(current_guess-number) <=50:
		print "cool"
		if previous_guess == 0:
			attempt = 1
		elif abs(current_guess-number) < abs(previous_guess-number):
			print "you're getting closer"
		elif abs(current_guess-number) > abs(previous_guess-number):
			print "you're getting further away"
		previous_guess = current_guess
	else:
		print "cold"
		if previous_guess == 0:
			attempt = 1
		elif abs(current_guess-number) < abs(previous_guess-number):
			print "you're getting closer"
		elif abs(current_guess-number) > abs(previous_guess-number):
			print "you're getting further away"
		previous_guess = current_guess