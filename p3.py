Amount_of_donuts = int(input("enter the number of donuts"))
events = int(input("enter the number of events: "))

current_event = 1
while current_event <= events and Amount_of_donuts >=0:
    event_type = input("+ or -")
    Amount_of_donuts = int(input("enter donut amount:"))
    if event_type == "+":
        donut_count + Amount_of_donuts
    elif event_type == "-": 
         donut_count = donut_count - Amount_of_donuts
    else: 
        print("invalid")
# end of code 

print("at the end of out eevtns, we have {donut_count}")
