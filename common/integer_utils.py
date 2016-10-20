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

def get_list_of_primes(n):
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]    

def get_triangular_number(index):
    return index * (index + 1) / 2
