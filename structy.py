from math import sqrt, floor

''' Find max number from the list '''


def max_value(nums):
    mx = float('-inf')
    for i in nums:
        if i > mx:
            mx = i

    return mx


''' Find given number is prime or not '''


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, floor(sqrt(n)) + 1):
        print(i)
        if n % i == 0:
            return False

    return True


''' Find duplicate in list '''


def contains_dupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            seen.add(item)
        else:
            print(item)
            return True


if __name__ == "__main__":
    my_list = [1, 2, 3, 2, 4, 5, 3, 6]
    contains_dupe(my_list)
