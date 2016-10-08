'''
'''

import sys
sys.path.append("common")
from integer_utils import *

class Solver:
    def get_result(self):
        sum = 0
        last_prime = 2
        while last_prime < 2000000:
            sum += last_prime
            last_prime = get_next_prime(last_prime)

        return sum


solver = Solver()
print(str(solver.get_result()))

