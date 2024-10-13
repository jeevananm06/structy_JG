def uncompress(s):
    result = []
    i = 0
    for i in range(0, len(s)):
        num = 0
        # Extract the number
        while s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
        # Extract the character
        char = s[i]
        i += 1
        # Append the character 'num' times to the result
        result.append(char * num)
    return ''.join(result)


# structy soln
def uncompress1(s):
    numbers = '0123456789'
    result = []
    i = 0
    j = 0
    while j < len(s):
        if s[j] in numbers:
            j += 1
        else:
            num = int(s[i:j])
            result.append(s[j] * num)
            j += 1
            i = j

    return ''.join(result)


print(uncompress1('112c3a1t'))
