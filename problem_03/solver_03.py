'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''
class Solver:
    
    def __is_prime(self, number):
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

    def __get_next_prime(self, number):
        next_number = number + 1
        if self.__is_prime(next_number):
            return next_number
        else:
            return self.__get_next_prime(next_number)

    def __is_divisor_of(self, divisor, number):
        return number % divisor == 0

    def __get_prime_factors_of(self, number):
        prime_factors = []

        target_number = number
        last_divisor = 2

        while (True): 
            if self.__is_divisor_of(last_divisor, target_number):
                prime_factors.append(last_divisor)
                quotient = float(target_number) / float(last_divisor)
                target_number = int(quotient)
                if quotient == 1:
                    break
            else:
                last_divisor = self.__get_next_prime(last_divisor)

        return prime_factors

    def get_result(self):
        prime_factors = self.__get_prime_factors_of(600851475143)
        return prime_factors[len(prime_factors)-1]