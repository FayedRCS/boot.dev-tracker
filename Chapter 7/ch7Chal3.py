#def has_enough_gas(gallons_in_car, miles_one_way, miles_per_gallon):
#    total_miles = gallons_in_car * miles_per_gallon
#    if total_miles >= miles_one_way*2:
#        return True
#    else:
#        return False

                            #Two ways to solve this problem. Codeblock above is my first though
                            #Second solution is more tailored to challenge preference
def has_enough_gas(gallons_in_car, miles_one_way, miles_per_gallon):
    gallons_needed = miles_one_way * 2
    gallons_available = gallons_in_car * miles_per_gallon
    if gallons_needed <= gallons_available:
        return True
    else:
        return False
