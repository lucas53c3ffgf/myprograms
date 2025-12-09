empty_string = ""
ver2 = ''
# method 1:
#determin if a string is empty 
if not str_var: 
    print("str_var is empty")

if len(str_var) == 0:
    print("str_var is empty")

#format a string to contain dynamic data 
name ="fluffington"
str_var =f"hello {name}"

#access individual characters/items in a string 
print(name[0]) # ---> f 
print(name[-2])# ---> o 

#acess the first. acess the last item in a string 
print(name[0])#alwasy first 
print(name[len(name)-1])#this gives last 
print(name[-1])#also gives last

#join two/multiple  strings together 
a = "poo"
b = "poo"
c = a + b 
print(c) # exptect poopoo 

#reverse a string 
temp = "park"
reversed_temp = temp[::-1]
v2 = ''.join(reversed(temp))
#create a copt of a string 
temp = "hydroflask"
temp_copy = temp[:]
another_copy = temp
#compare string for equality
a = "marshal"
b = "dog "
status = a == b
#determin the minumum and maximum values within a string 
temp = "hydroflask"
print(max(temp))
print(min(temp))
print(max('hello','goodbye'))
print(min('1','2','3'))

#determine if an item or a pattern exists within a string
word = poopooplatter 
if "poo" in word:
    print('there is poo')

#locate the index of an item or a patter within a string 
poop_location = word.find("poo")
poop_location = word.index("poo")

#count how often an item or a pattern occurs within a string 
poop_count = word.count("poo")
#convert all item in a string to uppercase/lowercase 
yell_hydroflash = "hydroflask".upper()
calm_hydroflask = yell_hydroflask.lower()
# determine if the string can be conveted to an integer 
str_num = "67"
if str_num.isdigit():
    num = int(str_num)

#convert a string to an integer 
word = "shsm".isalpha()

# removed non alphabetical chracters froma string 
#sometimes it is easier to create/grow thhan remove 
gibberish = "134g924g7h9f8jf2eujfw1j0jdifj29f2j"
clean = ""
i = 0 
while i < len(gibberish):
    if gibberish[i].isalpha():
        clean += gibberish[i]
    i += 1 

# remove all alhabetical charcters from a string 
gibberish = "134g924g7h9f8jf2eujfw1j0jdifj29f2j"
clean = ""
i = 0 
while i < len(gibberish):
    if gibberish[i].isalpha(): == False: # could have if not instead of adding False: at the end 
        clean += gibberish[i]
    i += 1 
