import random
from time import sleep
winner = "n"
difficulty = 1
def doWin(difficulty):
	if difficulty == 1 and winner == "y":
		print("You just won 10 tickets!")
	if difficulty == 2 and winner == "y":
		print("You just won 50 tickets")
	if difficulty == 3 and winner == "y":
		print("You just won a whopping 75 tickets!!")

def checkWin():
	if slot1 == slot2 == slot3:
		winner = "y"
		print("__--||CONGRATS! YOU WON!||--__")
	else:
		winner = "n"
		print("__--||Aw man, no dice!||--__")
	if winner == "y":
		doWin(difficulty)	
def doslotEasy():
	slot1 = random.randint(0, 2)
	slot2 = random.randint(0, 2)
	slot3 = random.randint(0, 2)
	checkWin()
def doslotMedium():
	slot1 = random.randint(0, 3)
	slot2 = random.randint(0, 3)
	slot3 = random.randint(0, 3)
	checkWin()
def doslotHard():
	slot1 = random.randint(0, 5)
	slot2 = random.randint(0, 5)
	slot3 = random.randint(0, 5)
	checkWin()
def mainMenu():
	print("Welcome to Asa and Gus' Slots!")
	sleep(0.5)
	print("Lets pay! err.. Play! ..heh heh..")
	print("|||MAIN) MENU|||")
	menuSelect = input("Type the number of the selection you want and hit enter \n" "1.Play with selected difficulty \n" "2.Select difficulty \n" "3.Phrase of the day")
	if menuSelect == 1:
		if difficulty == 1:
			print("One serving of easy mode coming right up!")
			sleep(0.7)
			doslotEasy()
		if difficulty == 2:
			print("Medium is squarley in your corner")
			sleep(0.7)
			doslotMedium()
		if difficulty == 3:
			print("Oh, a hardcore player eh?, good luck!")
			doslotHard()
	if menuSelect == 2:
		difficulty = input("Please enter your desired difficulty level from 1 to 3 with 3 being the harders and 1 being the easiest")
		mainMenu()
