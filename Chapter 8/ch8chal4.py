def is_prime(number):

    if number <= 0 or number == 1: #rules out negative numbers, as well as 0 and 1
        return False
    

    for i in range(2, number):
        if number % i == 0:
            return False

    return True

print(is_prime(3169))