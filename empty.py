#create an empty list 
a_list = []
b_list = list()
#determine if a string is empty 
if not a_list:
    print("a_list is empty!")

if len(a_list) == 0: 
    #what does len, sum, min, max do when list i 
c_list = [3,1,4,1,5,9]
print(len(c_list)) # except 6 
print(sum(c_list)) #23
print(min(c_list)) #1 
print(max(c_list)) #9

#access individual items in a list 
d_list = list("hello world!")
print(d_list[0]) # "h"
print(d_list[-1]) # "!"
print(d_list[1:4]) # e,l,l

#join two/multiple lists together 
a = [3,1,4]
b = ["marshal" , "freya" , "joy"]
c = a + b # createds a new lsit of a and b joined 
a.extend(b) # this mutates a to give contents to b 
a = [3,1,4]
for time in b:
    a.append(item)



