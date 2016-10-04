import sys
sys.path.append("common")
from integer_utils import *

'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''
class Solver:
    
    def __get_prime_factors_of(self, number):
        prime_factors = []

        target_number = number
        last_divisor = 2

        while (True): 
            if is_divisor_of(last_divisor, target_number):
                prime_factors.append(last_divisor)
                quotient = float(target_number) / float(last_divisor)
                target_number = int(quotient)
                if quotient == 1:
                    break
            else:
                last_divisor = get_next_prime(last_divisor)

        return prime_factors

    def get_result(self):
        prime_factors = self.__get_prime_factors_of(600851475143)
        return prime_factors[len(prime_factors)-1]