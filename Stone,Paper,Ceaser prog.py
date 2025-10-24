list=['s','p','c']
import random
t=random.choice(list)
a=0
b=0
c=0
while a<11:
    num=str(input("Press s for stone\nPress c for ceaser\nPress p for paper"))
    if num=="s" and t=="s":
        print(f"Its a tie!!!\nYour points={b}\ncomputers points={c}\nyou have taken{str(a+1)}attempts")
        b=b+0
        c=c+0
        a=a+1
    elif num=="s" and t=="p":
        print(f"You lost this match computer will get a point\nYour points={str(b+0)}\ncomputers points={str(c+1)}\nyou have taken{str(a+1)}attempts")
        b=b+0
        c=c+1
        a=a+1
    elif num=="s" and t=="c":
        print(f"You won this match you will get a point\nYour points={str(b+1)}\ncomputers points={str(c+0)}\nyou have taken{str(a+1)}attempts")
        b=b+1
        c=c+0
        a=a+1
    elif num=="c" and t=="s":
        print(f"You lost this match computer will get a point\nYour points={str(b+0)}\ncomputers points={str(c+1)}\nyou have taken{str(a+1)}attempts")
        b=b+0
        c=c+1
        a=a+1
    elif num=="c" and t=="p":
        print(f"You won this match you will get a point\nYour points={str(b + 1)}\ncomputers points={str(c+0)}\nyou have taken{str(a+1)}attempts")
        b=b+1
        c=c+0
        a=a+1
    elif num=="c" and t=="c":
        print(f"Its a tie!!!\nYour points={b}\ncomputers points={c}\nyou have taken{str(a+1)} attempts")
        b=b+0
        c=c+0
        a=a+1
    elif num=="p" and t=="c":
        print(f"You lost this match computer will get a point\nYour points={str(b+0)}\ncomputers points={str(c+1)}\nyou have taken{str(a+1)}attempts")
        b=b+0
        c=c+1
        a=a+1
    elif num=="p" and t=="s":
        print(f"You won this match you will get a point\nYour points={str(b + 1)}\ncomputers points={str(c+0)}\nyou have taken{str(a+1)}attempts")
        b=b+1
        c=c+0
        a=a+1
    elif num=="p" and t=="p":
        print(f"Its a tie!!!\nYour points={b}\ncomputers points={c}\nyou have taken{str(a+1)} attempts")
        b=b+0
        c=c+0
        a=a+1
    else:
        print("Incorrect input")
if a==11:
    if c==b:
        print(f"Match Tie\n your points={b}\nComputers points={c}\ntotal attempts taken={a}")
    elif c<b:
        print(f"you won the game!!!\n your points={b}\nComputers points={c}\ntotal attempts taken={a}")
    else:
        print(f"computer won the game\n your points={b}\nComputers points={c}\ntotal attempts taken={a}")
else:
    print("Something went wrong")





