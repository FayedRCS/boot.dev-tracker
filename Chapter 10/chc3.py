def calculate_total(items_purchased, grocery_list):

    item_prices = {
        "milk": 2.50,
        "eggs": 3.25,
        "bread": 1.21,
        "cheese": 3.50,
        "apples": 7.44,
        "bananas": 3.88,
        "carrots": 3.89,
        "lettuce": 1.12,
        "potatoes": 32.21,
        "cereal": 5.99,
    }

    # Don't touch above this line

    #start with the easiest; make a list of items in gorcery_list not found

    missing_items = []

    for i in grocery_list:
        if i not in items_purchased:
            missing_items.append(i)

    '''missing_items = ", ".join(missing_items)'''

    bought_items = {}

    for i in items_purchased:
        bought_items[i] = 0

    for match in bought_items:
        
        if match in item_prices:
            bought_items[match] = item_prices[match]


    sum_total = 0

    #iterate thought the dictionary and add the prices, this all assumes the price is listed for the item

    for price in bought_items:
        sum_total += bought_items[price]

    return missing_items, bought_items, sum_total


        
'''return print(f"The following were not bought: {missing_items}")'''
        #they want a boring return statement

test1 = ["eggs", "milk", "juice", "cheese",]
test2 = ["eggs", "milk", "juice", "cheese", "mustard", "scotch", "vinegar"]

print(calculate_total(test1, test2))

    