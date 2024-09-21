from math import sqrt, floor

''' Find max number from the list '''


def max_value(nums):
    return max(nums)


''' Find given number is prime or not '''


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, floor(sqrt(n)) + 1):
        print(i)
        if n % i == 0:
            return False

    return True
