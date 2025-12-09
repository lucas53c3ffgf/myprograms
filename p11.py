def clean(text): 
    # to reutrn a string with evrything lowercased 
    # and without special characgters nor numbers 
    result = ""
    i=0 # avoid index b/c it is a function/method name 
    while i < len(text):
        if text[i].isalpha():
            result = result + text[i].lower()
            #.isalpha() returns true if the given harcter is 
            #alphebetical 
        i += 1 
    return result 
word = input("what is your word to clean")
print(clean("p00p"))