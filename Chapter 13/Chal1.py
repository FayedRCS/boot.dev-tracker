def number_sum(n):

    sum_total = 0

    #assuming n is always an int we loop through indices 0 -> n + 1, adding each num to sum_total
    
    for num in range(0, n + 1):

        sum_total += num

    return sum_total

print(number_sum(5))

[1,2,3,4,5]