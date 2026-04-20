import random
print("Welcome to the Number Guessing Game!")
print("Choose a number between 1-50")
print("You only have 6 tries")
a = random.randint(1, 50)
for i in range(1, 7):
    b = int(input(f"Trial {i}: "))
    c=a-b
    if c == 0:
        print("Correct! Congratulations!")
        print("Your score:", (7 - i), "/6")
        break
    elif 20<c<=30:
        print("Too far. Go higher.")
    elif 10<c<=20:
        print("Getting nearer. Go higher.")
    elif 0<c<=10:
        print("Very close! Slightly higher.")
    elif -10<=c<0:
        print("Very close! Slightly lower.")
    elif -20 <= c < -10:
        print("Getting nearer. Go lower.")
    elif -50 <= c < -20:
        print("Too far. Go lower.")
    else:
        print("Out of range!")

    print(6 - i, "tries left")

else:
    print("Game Over! The number was", a)