
from random import choice #choice is a function that randomly chooses from a list 
while True:
    print("welcome to our heads orr tails game!")
    print("please choose either heads or tails")
    while True: 
        user_input = input("user's choice:")
        user_input = user_input.lower() # immutability a data type or an object that cannot mutate 

        if user_input in {"head", "tails", "heads", "tails"}:

            break # allows us to exit a lopping structure 
        else: 
            print("please type in heads or tails, :) ")

    #end of while 
    flip_result = choice(["head", "tails"])

    print(f"the computer flipped")
    if user_input in {"heads", "head"} and flip_result == "heads": 
        print("the user guessed correctly")
    elif user_input in {"tails", "tail"} and flip_result == "tails": 
        print("the user guessed correctly")
    else: 
        print("you guessed wrong")
    
    
   



