def double_string(string):

    #setting an empty array, to append each letter in the string, twice.
    first = []
    
    for letters in string:
        first.append(letters)
        first.append(letters)

    #joining the indexes of the list together, no "delimiter", we just want to join them, and assign it to a new "empty" variable.

    string_version = "".join(first)

    #print(string_version)

    return string_version


