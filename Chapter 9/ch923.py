# nivå 6
def reverse_array(items):
    
    #
    reversed_list= []

    for i in range(len(items)-1, -1, -1):
        reversed_list.append(items[i])

    return reversed_list


# slicing alternative: return items[::-1] instead of #-#