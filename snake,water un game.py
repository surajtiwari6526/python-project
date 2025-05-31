'''
1 for snake
-1 for water
0 for gun
'''
import random as rand
computer=rand.choice([-1,0,1])
print("enter your choice w is for water,s is for snake , and g  is for gun:")
yourstr=input("enter yor choice:")
youdict={"s":1,"w":-1,"g":0}
you=youdict[yourstr]
if computer==you:
    print("draw")
else:
    if computer==-1 and you==1:
        print("you won the game")
    elif computer==-1 and you==0:
        print("you lose the game")
    elif computer==1 and you==-1:
        print("you lose the game")
    elif computer==-1 and you==0:
        print("you won the game")
    elif computer==0 and you==-1:
        print("you won the game")
    elif computer==0 and you==-1:
        print("you lose the game")
    # else:
    #     print("something went wrong")
    