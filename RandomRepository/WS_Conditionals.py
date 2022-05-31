legal_driving_age = 16
your_age = int(input("What is your age?"))
if(your_age >= legal_driving_age):
    print("You are legally able to drive.")
elif(your_age < legal_driving_age):
    print("You are not old enough to drive yet.")

import random

random_number = random.randrange(0,11)

print(random_number)

if(random_number == 0) or (random_number == 1) or (random_number == 2):
    print("0 or 1 or 2")
elif(random_number == 3) or (random_number == 4) or (random_number == 5):
    print("3 or 4 or 5")
elif(random_number == 6) or (random_number == 7) or (random_number == 8):
    print("6 or 7 or 8")
elif(random_number == 9) or (random_number == 10):
    print("9 or 10")

football_team = input("Which is your favorite football team? ")

if(football_team == "Bears "):
    print("Quarterback much? ")
elif(football_team == "Vikings "):
    print("Loud noises!")
elif(football_team == "Lions "):
    print("LOL They bad!")
elif(football_team == "Packers "):
    print("Best team in the world! Actually, the universe! ")
else: 
    print("You should be an Eagles fan")



