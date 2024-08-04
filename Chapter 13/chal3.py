def remove_nonints(nums):
    
    integer_list = []

    #check the type of a variable using type() function

    for types in nums:
        if type(types) == int:
            #appending to the empty list, tasks wants a completely new list
            integer_list.append(types)
    
    return integer_list
