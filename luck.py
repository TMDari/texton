import random
import time
import os
I = 0
loop = 1
T = 1 
while loop==1:
	
	print("-|Lucky Chip|-")
	print("")
	print("1.Coinflip")
	print("2.Dice")
	I = int(input("Type a number"))
	os.system('cls' if os.name == 'nt' else 'clear')

	if I==1:
		coin = random.randrange(0,2)
		if coin==0:
			print("Head")
		if coin==1:
			print("Tail")
	if I==2:
		dice = random.randrange(1,7)
		print(str(dice))
		
	time.sleep(T)
	loop = int(input("Go again? 1=yes 0=no"))
	if loop==0:
	    print("Closing programm")
	    time.sleep(T)
	os.system('cls' if os.name == 'nt' else 'clear')

	