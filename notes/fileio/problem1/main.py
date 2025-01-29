import random

def game():
    print("Hello you are now pllaying a game! ...")
    score = random.randint(1, 99)
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if (hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0        
    if (score>hiscore):
        with open("hiscore.txt", "w") as f:
            f.write(str(score))
    print(f"Your current score is {score}")
    return score

game()


