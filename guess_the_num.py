import random
n = random.randint(1,10)
guess = 0
while guess!=n:
    guess=int(input("enter a number: "))
    if guess<n:
        print("it is samller")
    elif guess>n:
        print("it is larger")
    else:
        print("correct guess")