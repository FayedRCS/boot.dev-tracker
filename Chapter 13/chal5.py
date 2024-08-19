def area_sum(rectangles):
    
    lst = []

    for rect in rectangles:
  
        lst.append(rect["width"] * rect["height"])
        
    return sum(lst)

test = [{"height": 2, "width": 3}, {"height": 4, "width": 5}]
area_sum(test) 

