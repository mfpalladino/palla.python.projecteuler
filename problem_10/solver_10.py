'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

import sys
sys.path.append("common")
from integer_utils import *

class Solver:
    def get_result(self):
        primes = get_list_of_primes(2000000)
        sum = reduce(lambda x, y: x + y, primes)

        return sum