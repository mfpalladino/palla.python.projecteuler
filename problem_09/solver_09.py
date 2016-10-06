'''
Special Pythagorean triplet
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

class Solver:
    def get_result(self):
        should_continue = True
        max_count = 999
        final_a = 0
        final_b = 0
        final_c = 0
        for a in range(1, max_count):
            if should_continue == False:
                break
            for b in range(1, max_count):
                if should_continue == False:
                    break
                for c in range(1, max_count):
                    is_pythagorean_triplet = pow(a,2) + pow(b,2) == pow(c,2)
                    if is_pythagorean_triplet:
                        if (a + b + c == 1000):
                            final_a = a
                            final_b = b
                            final_c = c
                            should_continue = False
                            break
                            
        return final_a * final_b * final_c