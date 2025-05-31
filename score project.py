import random
def game():
    print("you are playing a game...")
    score=random.randint(1,100)
    #fetch the high score
    with open ("score.txt") as f:
        highscore=f.read()
        if highscore!="":
            highscore=int(highscore)
        else:
            highscore=0
    
    print(f"your score is{score}")
    if score>highscore :
      #write his score in the file
      with open("score.txt","w") as f:
          f.write(str(score))
    return score

game()
