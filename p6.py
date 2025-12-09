


square= 1 
while True: 
    roll = int(input("enter doce roll data:"))

    if square + roll = 100: 
        print(f"you are on square {square + roll}")
        print("you win")

    else: 
        new_position = square + roll

        game_dict = {
            9 : 34, 
            54 : 19, 
            40 : 64, 
            90 : 48, 
            67 : 86, 
            99 : 77
        }
        if new_position in game_dict:
            square = game_dict[new_position]
        else: 
            square += roll

        if new_position ==9: 
            square = 34 
        else new_position ==54: 
            square = 19 




