# 8. Write a function, is_prime, that takes an integer and returns True if
# the number is prime and False if the number is not prime.

import math


def is_prime(num):
    if num > 1:
        for i in range(2, int(math.sqrt(num)+1)):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False


print(is_prime(127661))
