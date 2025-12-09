def is_nagaram(a_list,b_list):
    while len(a_list) == len(b_list)
        return true 
    else: 
        return false 
    



#solution
def anagram_check(word1,word2):
    # technique -> frewuency table 
    # letter:count 
    freq_table = {}#empty dict 
    for c in word1:
        if c in freq_table:
            freq_table[c] +=1
        else:
            freq_table[c] = 1

    for c in word2:
        if c not in freq_table:
            return False
        else:
            freq_table[c] -= 1 
            if freq_table[c] < 0:
                return False

    for key, value in freq_table.item():
        if value != 0:
            return False 
    
    return True 


# recurssion, Write a recursive function that evaluates the power to its integer representation. 
#2^4 = 2 x 2 x 2 x 2 = 16

def interget(base,power):

#solution 
def exponent(base,exp):
    if exp = 0:
        return 1 
    elif exp == 1:
        return base 
    else:
        return base * exponent(base,exp-1)


#missing number question 

def num(num_list):
    num = [3,0,1]
    for i in range(0, len(num_list)):
        return 

#solution 
def missing(array):
    limit = len(array)
    freq_table = {}
    for x in array:
        freq_table[x] = 1 
    
    for i in range(0,limit+1):
        if i not in freq_table:
            return 1 
    return -1

    #another solution (but alot slower then the solution above)
    for i in range(0,limit+1):
        if i not in array:
            return 1
    


#scrabble question 

 
    

    



    



