def area_sum(rectangles):
    #empty list for each seperate area sum...
    lst = []
    total = 0

    for dicts in rectangles:

        retangle_area = 1

        for value in dicts:
            retangle_area *= dicts[value]

        lst.append(retangle_area)

    #adds all elements in lst

    for sum in range(0, len(lst)):
        total = total + lst[sum]

    return total

test = [{"height": 2, "width": 3}, {"height": 4, "width": 5}]
area_sum(test) 

            
            
        


