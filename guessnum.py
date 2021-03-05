import random

correcta = random.randint(1, 100)

gameover = False

while gameover == False:
    playerg = int(input("Guess a number between 1 and 100: "))

    if playerg == correcta:
        comparea = "Right"
        gameover = True
        print("Correct! You Win!")
    elif playerg > correcta:
        comparea = "High"
        print("Too high! Guess Again!")
    elif playerg < correcta:
        comparea = "Low"
        print("Too low! Guess again")


# mi10+
