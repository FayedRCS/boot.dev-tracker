def factorial(num):

    #set starting to 1, not 0.
    
    calc_factorial = 1
    
    #range is essential here to get the right result. I use decrementing step to easily visualize the factorial (4! = 4 * 3 * 2 * 1)

    for i in range(num, 0, -1):
        calc_factorial *= i

    return calc_factorial






