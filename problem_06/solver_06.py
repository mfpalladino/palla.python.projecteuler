'''
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten 
natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred 
natural numbers and the square of the sum.
'''

class Solver:
    def get_result(self):
        sum_of_squares = 0
        sum_of_numbers = 0
        for i in range(1, 100+1):
            sum_of_squares += pow(i,2)
            sum_of_numbers += i

        square_of_sum_of_numbers = pow(sum_of_numbers,2)
        return square_of_sum_of_numbers - sum_of_squares
