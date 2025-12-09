def clean(text): 
    # to reutrn a string with evrything lowercased 
    # and without special characgters nor numbers 
    result = ""
    i = 0 # avoid index b/c it is a function/method name 
    while i < len(text):
        if text[i].isalpha():
            result = result + text[i].lower()
            #.isalpha() returns true if the given harcter is 
            #alphebetical 
        i += 1 
    return result 
word = input("what is your word to clean")
print(clean("p00p"))

'''
let x represent a string, t be a target cjaracter to search 
let I represent index of a string 
while i < len(x), if x[i] == T then return i else i + 1 
if T is not dound, return -1 \
''' 
def str_lin_search(text, target): 
    if not text: # len(text) == 0  
        return -1 
    else: 
        i = 0
        while i < len(text):
            if text[i] == target:
                return i 
            i += 1 
        # end of whike 
        return -1 

print(" where is p?", str_lin_search("jasper","p"))
        


#  give 2 searching alogrithms, always on ib exam 














