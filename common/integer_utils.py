def is_prime(number):
    #using division by trying
    if number == 2:
        return True
    
    is_even = number % 2 == 0
    if number < 2 or is_even:
        return False
    
    result = True
    for i in range(3, number):
        if number % i == 0:
            result = False
            break

    return result

def get_next_prime(number):
    next_number = number + 1
    if is_prime(next_number):
        return next_number
    else:
        return get_next_prime(next_number)

def is_divisor_of(divisor, number):
    return number % divisor == 0