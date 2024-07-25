def meditate(mana, max_mana, energy, energy_potions):
    while (energy > 0 or energy_potions > 0) and mana < max_mana:
        if energy == 0:
            if energy_potions > 0:
                energy_potions -= 1
                energy += 50
            else:
                break
        
        energy -= 1
        mana = mana + 3
        if mana > max_mana:
            mana = max_mana

    return mana, energy, energy_potions
        
        
    #energy = mana * 3
    #mana <= max_mana
    #energy_potions = energy * 50