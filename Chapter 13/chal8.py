def join_strings(strings):

    joined = ""
    
    for string in strings:

        joined += string + ","

    
    #slice the comma out, as it places one after every element

    joined = joined[:-1]

    return joined