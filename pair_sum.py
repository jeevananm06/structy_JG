def pair_sum(numbers, target_sum, ret):
    previous_numbers = {}

    for index, num in enumerate(numbers):
        complement = target_sum - num

        if complement in previous_numbers:
            if ret == 'index':
                return (index, previous_numbers[complement])
            elif ret == 'boolean':
                return True
            else:
                return complement, num

        previous_numbers[num] = index
    return False


print(pair_sum([3, 2, 5, 4, 1], 8, 'value'))
