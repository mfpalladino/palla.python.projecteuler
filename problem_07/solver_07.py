'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10001st prime number?
'''

import sys
sys.path.append("common")
from integer_utils import *

class Solver:
    def get_result(self):
        count_of_primes = 1
        last_prime = 2
        while count_of_primes < 10001:
            last_prime = get_next_prime(last_prime)
            count_of_primes += 1

        return last_prime

