from inputimeout import inputimeout as inputt
import random as r, os, fontstyle as ft, time
mode1 = ['a','b','c','d','e','f','g','h','i','j','k','l','n','m','o',
'p','q','r','s','t','u','v','w','x','y','z']
mode2 = [1,2,3,4,5,6]
mode3 = [0,0,1] 
score = 0
loop=0

title = ft.apply("SEND", "BOLD, UNDERLINE") + ft.apply("!","RED,BOLD")+"V.1.0\n■■■■■■"

menu = title+ft.apply("\n1. Alphabet\n2. Zones\n3. Exit\n","BOLD")
fail = title+'\n'+ft.apply('Game Over!','RED,BOLD')+ft.apply('\nScore:','BOLD')

v1 = r.choice(mode1)
v2 = r.choice(mode2)
v3 = r.choice(mode3)
clock = 3

os.system('cls' if os.name == 'nt' else 'clear')

def mode2vis(val):
    if val==1:
        visual="1  2  3\n■□□\n□□□\n4  5  6"
    elif val==2:
        visual="1  2  3\n□■□\n□□□\n4  5  6"
    elif val==3:
        visual="1  2  3\n□□■\n□□□\n4  5  6"
    elif val==4:
        visual="1  2  3\n□□□\n■□□\n4  5  6"
    elif val==5:
        visual="1  2  3\n□□□\n□■□\n4  5  6"
    elif val==6:
        visual="1  2  3\n□□□\n□□■\n4  5  6"
    return "\n"+visual

def gamestart():
    clock = 3
    score = 0
    os.system('cls' if os.name == 'nt' else 'clear')
    print(title+"\n\nReady")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(title+"\n\nSet")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(title+"\n\nGO!")
    time.sleep(1)


while loop==0:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(menu)
    try:
        loop = int(input("select: "))
    except Exception:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("type a number from 1 to 4!")
        womp=input("press enter to go back!")
    if loop!=3:
        gamestart()
    while loop==1:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            v1 = r.choice(mode1)
            a = inputt(prompt=
            title+ft.apply("\nScore:","BOLD")+
            str(ft.apply(score,"YELLOW,BOLD"))+
            ft.apply("\ntype ","BOLD")
            +v1+"\ntime:"+str(clock)+"\n: ", timeout=clock)
        except Exception:
            a = 'end'
        if a==v1:
            score = score+1
            if clock>=1:
                clock=round(clock-0.05,2)
            if clock<1.05:
                score = score+1
                
            
        elif a!=v1 or a=='end':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(fail+
            ft.apply(str(score),"BOLD,YELLOW")+
            ft.apply("\nfail:","BOLD")+v1)
            loop=0
            womp = input("\npress enter to go back!")


    while loop==2:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            v1 = r.choice(mode2)
            v2 = mode2vis(v1)
            a = inputt(prompt=
            title+ft.apply("\nScore:","BOLD")+
            str(ft.apply(score,"YELLOW,BOLD"))+
            v2+"\ntime:"+str(clock)+"\n: ", timeout=clock)
        except Exception:
            a = 'end'
        if a==str(v1):
            score = score+1
            if clock>=1:
                clock=round(clock-0.05,2)
                
        elif a!=str(v1) or a=='end':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(fail+
            ft.apply(str(score),"BOLD,YELLOW")+
            ft.apply("\nfail:","BOLD")+str(v1))
            loop=0
            womp = input("\npress enter to go back!")