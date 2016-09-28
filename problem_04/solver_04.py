'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit 
numbers is 9009 = 91 * 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

class Solver:

    def __is_palindrome(self, number):
        number_as_string = str(number)
        length = len(number_as_string)
        if length % 2 != 0:
            return False

        result = True    
        for i in range(0,length/2):
            if number_as_string[i] != number_as_string[length-1-i]:
                result = False
                break 

        return result

    def __get_largest_palindrome_from_interval(self, begin, end):
        largest_palindrome = 0
        for i in range(begin, end + 1):
            for j in reversed(range(begin, end + 1)):
                target_number = j * i
                if self.__is_palindrome(target_number):
                    if target_number > largest_palindrome:
                        largest_palindrome = target_number
                    break

        return largest_palindrome

    def get_result(self):
        return self.__get_largest_palindrome_from_interval(100, 999)
