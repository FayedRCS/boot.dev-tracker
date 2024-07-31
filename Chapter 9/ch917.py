def get_champion_slices(champions):
    return champions[2:], champions[0:-2], champions[::2]


print(get_champion_slices([1,2,3,4,5]))
