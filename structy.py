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


def anagrams(s1, s2):
    return (chr_count(s1) == chr_count(s2))


def chr_count(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count


# print(anagrams('paper', 'reapa'))


''' Find frequent used chars'''


def most_frequent_char(s):
    mx = 0
    for k, v in chr_count(s).items():
        if mx < v:
            mx = v
            key = k
    return key


print(most_frequent_char('bookeeper'))
