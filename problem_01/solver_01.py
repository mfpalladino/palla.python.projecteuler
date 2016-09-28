'''
Problem 1
Multiples of 3 and 5
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''

def solver():
    index = 1
    sum = 0
    while index < 1000:
        multipleOf3 = index % 3 == 0
        multipleOf5 = index % 5 == 0

        if (multipleOf3 or multipleOf5):
            sum += index

        index += 1
    
    return sum

