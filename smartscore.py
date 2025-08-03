#Build a Python script that:
#- Asks a user to input a score (0–100)
#- Classifies the score into a grade (A, B, C, D, F)
#- Gives a motivational message for each grade
#- Optionally checks for invalid input (like negative or >100)
def smarscore():
    number=int(input("Enter Score:"))
    if number >= 80:
        print("You have an A for Apple")
    elif number >= 70:
        print("You have an B for Ball")
    elif number >= 60:
        print("You have an C for Cat")
    elif number >= 50:
        print("You have an D for Doll")
    elif number >= 40:
        print("You have an F for Flower")
    else:
        print("Too low")
smarscore()
