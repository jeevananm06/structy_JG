def find_local_maxima(data):
    mxim = []
    n = len(data)

    if n == 1:
        return [0]

    if n >= 2:
        if data[0] > data[1]:
            mxim.append(0)
        if data[n - 1] > data[n - 2]:
            mxim.append(n - 1)

    for i in range(1, n - 1):
        if data[i] > data[i - 1] and data[i] >= data[i + 1]:
            mxim.append(i)

    return mxim


data = [1,5, 3, 1, 2, 4, 2, 6, 2, 1]
maxima = find_local_maxima(data)

print("Local maxima positions:", maxima)

print("Local maximas:", [data[i] for i in maxima])

# print(local_maximun([5, 3, 1, 2, 4, 2, 6,2,2]))
# print(find_local_maxima([1, 3, 1, 2, 4, 2, 6, 9]))
# 1, 3, 1, 2, 4, 2, 6, 6
# 1, 1, 2, 3, 4, 2, 2
# 1, 3, 1, 2, 4, 2, 6, 9, 3,3
# original_string = "example"
# bracketed_string = f"({original_string})"
# print(bracketed_string)  # Output: [example]
