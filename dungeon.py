import random
import math
clear()
print ("*|TEXT DUNGEON|*")
print ("1. Start")
print ("2. give up :P")
print ("")
print("this game is very outdated.")
menu = int(input("Type the number to select..."))
if menu==1:
  print("you are entering the dungeon...")
elif menu==2:
  print("Game over!")
else:
  print(menu + " is not an option.")
  print("you may restart the game for being foolish")

if menu==1:
  room = 0
  life = 100
  damage = 1
  spawn = 0
  story = 0
  trap=1
  while room<15:
    time.sleep(0.5)
    clear()
    room = random.randrange(0,10)
    if room==2:
        print("You found a very unique dungeon room.")
        print("after admiring it for a while, you leave.")
    if room==3:
        story = story + 1
        if story==1:
            print("You heard a noise behind you...")
        elif story==2:
            print("You noticed something is following you...")
        elif story==3:
            print("Something threw a rock at you?!")
            print("it didn't affect you.")
        elif story==4:
            print("You turn around to find a confused Slime.")
            print("It looks at you and follows you around.")
        elif story==5:
            print("the slime protected you from a trap!")
            print("you no longer risk falling into traps!")
            trap=0
        elif story==6:
            print("You decided to name the slime bob.")
        elif story==7:
            print("the slime left... you can't find it anymore.")
            print("traps are a risk again.")
            trap=1
        elif story>7:
            print("You remember bob.")
        time.sleep(3)
        
    elif room==4:
      print("There are two doors.\n")
      print("1. go through the first.")
      print("2. go through the second.")
      way = int(input("Type the number to select..."))
      clear()
      print("you go through the selected door")
      time.sleep(2)
    elif room==5:
      print("There are three doors.\n")
      print("1. go through the first.")
      print("2. go through the second.")
      print("3. go through the third.")
      way = int(input("Type the number to select..."))
      clear()
      print("you go through the selected door")
      time.sleep(2)
    elif room<6:
      spawn = random.randrange(0,11)
      if spawn == 1:
          print("A goblin stole your weapon!")
          print("Damage is back to 1.")
          damage = 1
      elif spawn in [2,3,4] :
        print("You found a better weapon")
        damage = 1 + int(damage)
        print("you now make ", damage, " damage!")
        time.sleep(2)
      elif spawn == 5:
        print("You found a resting spot")
        time.sleep(1)
        if life<100:
          print("you used it to fully heal")
          life = 100
        else:
          print("but you dont need it")
      elif spawn in [7,8]:
        print("you walk into a trap")
        if trap==1:
            life = int(life) - 10
            print("your life is down to ", life)
        else:
            print("The Slime protected you.")
        if life==0:
          print("Game over!")
          room = 11
      elif spawn in [6,9,10]:
      	enemie = random.randrange(1,10)
      	print("an enemie with " ,enemie," life attacks you")
      	if enemie<=damage:
      		print("you killed it.")
      		print("luckily it was too slow to attack")
      	
      	elif enemie<=damage:
          	while enemie>=0 and life>=0:
          		
          		life = int(life) - 10
          		print("you hit the enemie")
          		print("it hit you")
          		print("your life:" , life)
          		enemie = int(enemie) - int(damage)
          		if enemie<=0:
          			print("you killed it.")
          		if life==0:
          			print("it killed you.")
          			print("Game over!")
          			room = 11
      time.sleep(2)
    elif room==1:
      print("You found an exit!")
      print("Game Won!")
      room = int(input("restart? 1=yes 2=no"))
      if room==2:
          room = 16