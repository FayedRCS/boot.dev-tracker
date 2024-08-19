def remove_duplicates(spells):
    
    removal = set()
    new_list = []

    for spell in spells:
        removal.add(spell)

    for append in removal:
        new_list.append(append)

    
    return new_list


my_val = {}

print(type(my_val))