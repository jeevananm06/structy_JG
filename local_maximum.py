def local_maximun(s):
    k = {}
    mx = s[0]
    length = len(s)
    for i, val in enumerate(s):
        if mx > val and s[i - 1] != mx:
            k[s[i - 1]] = i - 1
            mx = val
        else:
            if i + 1 == length and s[length-1] != val:
                k[s[i]] = i
            if i + 1 == length and (list(k.items())[-1])[0] <= val:
                k[s[i]] = i
            mx = val

    return k




def find_local_maxima(lst):
    local_maxima = []
    for i in range(1, len(lst) - 1):
        if lst[i] > lst[i - 1] and lst[i] > lst[i + 1]:
            local_maxima.append(lst[i])
    return local_maxima


print(local_maximun([5, 3, 1, 2, 4, 2, 6,2,2]))
# print(find_local_maxima([1, 3, 1, 2, 4, 2, 6, 9]))
# 1, 3, 1, 2, 4, 2, 6, 6
# 1, 1, 2, 3, 4, 2, 2
# 1, 3, 1, 2, 4, 2, 6, 9, 3,3
# original_string = "example"
# bracketed_string = f"({original_string})"
# print(bracketed_string)  # Output: [example]
