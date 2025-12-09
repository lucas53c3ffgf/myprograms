def perfect_number(num):
    divider = 1 
    total = 0 
    while divider < num: 
        if num % divider ==0: 
            total += divider 
        divider += 1 
    return total == num 
#end of is_perfect 
num = 1 
while num <= 1000000
    if perfect_number(num): 
    # if perfect_nunber(number) == True: 
        Print(f"{num} is perfect.")
    num += 1 


    