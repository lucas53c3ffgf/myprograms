def select (a_list): 
    if len(a_list) <= 1:
        return a_list
    else: 
        i = 0 
        while i < len(a_list):
            smallest = a_list[i] #prove it is or it's not the smallest

            j = i + 1 
            while j < len(a_list):
                new_value = a_list[j]
                if new_value < smallest: 
                    smallest = new_value 
                    new_location = j 
                j += 1 
            
#swap smallest into proper location 
            temporary = a_list[i]
            a_list[i] = smallest 
            a_list[new_location] = temporary 
            #python way 
            a_list[i], a_list[new_location] = a_list[new_location], a_list[i]
            i += 1




