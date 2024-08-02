def get_most_common_enemy(enemies_dict):
    
    if not enemies_dict:
        return

    common_enemy = float("-inf")

    for enemy in enemies_dict:

        #accesses the value, in the key-value pair
        enemies_met = enemies_dict[enemy]

        if enemies_met > common_enemy:
            common_enemy = enemies_met
            name = enemy #the key
    
    return name


