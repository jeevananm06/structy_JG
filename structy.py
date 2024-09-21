from math import sqrt,floor

def max_value(nums):
  return max(nums)

def is_prime(n):
  if n < 2:
    return False
  for i in range(2, floor(sqrt(n)) + 1):
    print(i)
    if n % i == 0:
      return False
    

  return True
