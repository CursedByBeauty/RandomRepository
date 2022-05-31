

import random
confirm_trip = ""
while confirm_trip != "y":
    destination = ['Lancaster', 'Strasburg', 'Paradise', 'Intercourse', 'Fertility']
    random_destination_from_list = random.choice(destination)

    confirmation_destination = input(f"Does {random_destination_from_list} sound like a fun destination? Enter y/n: ")


    while confirmation_destination != "y":

        if(confirmation_destination == "n"):
                print("Let's try again shall we?")
                random_destination_from_list = random.choice(destination)
            
        else:
                print("Please answer with 'y' or 'n'.")
        confirmation_destination = input(f"Does {random_destination_from_list} sound like a fun destination? Enter y/n: ")

    if(confirmation_destination == "y"):
        print("Awesome!")

    restaurant = ['Olde Mill Restaurant', 'Smokestack BBQ', 'Witmer Ox Roast', 'Fireside Tavern', 'Katies Kitchen']
    random_restaurant_from_list = random.choice(restaurant)

    confirmation_restaurant = input(f"Would you like to eat at {random_restaurant_from_list}? Enter y/n: ")


    while confirmation_restaurant != "y":

        if(confirmation_restaurant == "n"):
                print("Let's try again shall we?")
                random_restaurant_from_list = random.choice(restaurant)
        
        else:
            print("Please answer with 'y' or 'n'.")
            
        confirmation_restaurant = input(f"Would you like to eat at {random_restaurant_from_list}? Enter y/n: ")   

    if(confirmation_restaurant == "y"):
            print("Cool!")


    transportation = ['Car', 'Bus', 'Train', 'Walking', 'Airplane']
    random_transportation_from_list = random.choice(transportation)

    confirmation_transportation = input(f"Would you like to get there via {random_transportation_from_list}? Enter y/n: ")

    while confirmation_transportation != "y":

        if(confirmation_transportation == "n"):
                print("Let's try again shall we?")
                random_transportation_from_list = random.choice(transportation)
        else:
                print("Please answer with 'y' or 'n'.")
            
        confirmation_transportation = input(f"Would you like to get there via {random_transportation_from_list}? Enter y/n: ") 

    if(confirmation_transportation == "y"):
            print("Nice!")


    entertainment = ['the Amusement Park', 'Square Dancing', 'Go Kart Racing', 'Mini Golf', 'Horse Buggy Riding']
    random_entertainment_from_list = random.choice(entertainment)

    confirmation_entertainment = input(f"Does {random_entertainment_from_list} sound like something you would want to spend your time doing? ")

    while confirmation_entertainment != "y":

        if(confirmation_entertainment == "n"):
            print("Let's try again shall we?")
            random_entertainment_from_list = random.choice(entertainment)
        else:
            print("Please answer with 'y' or 'n'.")
            
        confirmation_entertainment = input(f"Does {random_entertainment_from_list} sound like something you would want to spend your time doing? ")

    if(confirmation_entertainment == "y"):
        print("Lovely!")


    confirm_trip = input(f"We have a trip to {random_destination_from_list} where you'll be eating at {random_restaurant_from_list} arriving by {random_transportation_from_list} as you spend your time {random_entertainment_from_list}. Does this sound good? Enter y/n: ")


        
    if(confirm_trip == "n"):
        print("I'm sorry, let's start from the top.")
    elif(confirm_trip == "y"):
        print("Perfect!")        
    else:
        print("Please answer with 'y' or 'n'.")

    

confirm_trip = print("Have a fun trip!")











