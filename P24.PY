def mergSort(a_list):
    # consider me as the splitter
    #Base case 
    if len(a_list) <= 1:
        return a_list
    
    #word towards the base case 

    mid = len(a_list) // 2
    first_half = a_list[:mid]
    second_half = a_list[mid:]

    first_half = mergSort(first_half) #recursive call 
    second_half = mergSort(second_half) # recursive call

    return combine(first_half,second_half)

def combine(left,right):
    #assume left and right are sorted 
    if len(left) == 0 and len(right) == 0:
        return[]
    elif len(left) == 0:
        return right
    elif len(right) == 0:
        return left
    else:
        #both elft and righ has values
        i = 0
        j = 0
        answer = [] # we shove the sorted stuff here
        while i <len(left) and j < len(right):
            if left[i] < right[j]:
                answer.append(left[i])
                i += 1 
            else:
                answer.append(right[j])
                j += 1
            #what happend if we have values leftover 
            while i < len(left):
                answer.apped(left[i])
                i += 1 
            while j < len(right[j]):
                answer.append(right[j])
                j += 1
            
            return answer 
            