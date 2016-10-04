'''
2520 is the smallest number that can be divided by each of the numbers 
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers 
from 1 to 20?
'''

class Solver:

    def __get_smallest_evenly_divisible_in_interval(self, interval_start, interval_end):
        number = 1
        go_to_infinite_hell = True

        while go_to_infinite_hell: 
            is_evenly_divisible = True
            for i in range(interval_start, interval_end + 1):
                if number % i != 0:
                    is_evenly_divisible = False
                    break
            
            if is_evenly_divisible:
                go_to_infinite_hell = False
            else:
                number += 1

        return number

    def get_result(self):
        result = self.__get_smallest_evenly_divisible_in_interval(1, 20)
        return result     