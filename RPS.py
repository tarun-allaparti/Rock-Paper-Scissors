import random

def computer():
	"""Creates game mode for playing against the computer by randomizing a choice and comparing to the user's input """
	print("rock...")
	print("paper...")
	print("scissors...")
	player1 = input("Make your move: ")
	player2 = random.choice(["rock","paper","scissors"])
	print("The computer plays " + player2)
	if player1 == player2:
		print("Tie!")
	elif player1 == "rock":
		if player2 == "paper":
			print("You lose!")
		elif player2 == "scissors":
			print("You win!")
		else:
			print("Wrong input")
	elif player1 == "paper":
		if player2 == "scissors":
			print("You lose!")
		elif player2 == "rock":
			print("You win!")
		else:
			print("Wrong input")
	elif player1 == "scissors":
		if player2 == "rock":
			print("You lose!")
		elif player2 == "paper":
			print("You win!")
		else:
			print("Wrong input")
	else:
		print("Wrong input")

def friend():
	"""Creates a game mode for playing against a friend by comparing the inputs for each player"""
	print("rock...")
	print("paper...")
	print("scissors...")
	player1 = input("Player 1, make your move: ")
	print("***********************    DON'T CHEAT!    *************************\n\n" * 30)
	player2 = input("Player 2, make your move: ")
	if player1 == player2:
		print("Tie!")
	elif player1 == "rock":
		if player2 == "paper":
			print("player2 wins!")
		elif player2 == "scissors":
			print("player1 wins!")
		else:
			print("Wrong input")
	elif player1 == "paper":
		if player2 == "scissors":
			print("player2 wins!")
		elif player2 == "rock":
			print("player1 wins!")
		else:
			print("Wrong input")
	elif player1 == "scissors":
		if player2 == "rock":
			print("player2 wins!")
		elif player2 == "paper":
			print("player1 wins!")
		else:
			print("Wrong input")
	else:
		print("Wrong input")


print("Welcome to rock paper scissors!")
play = "y"
while play == "y":
	game_mode = input("Do you want to play against the computer or against a friend? (computer/friend.)")
	if game_mode == "computer":
		computer()
	elif game_mode == "friend":
		friend()
	else:
		print("That's not a valid game mode.")
	play = input("Would you like to play again? (y/n)")
print("Thanks for playing!")






