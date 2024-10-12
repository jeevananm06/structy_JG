def uncompress(s):
    j=''
    for i in range(0, len(s), 2):
        k = s[i:i + 2]
        j += int(k[0])*k[1]
    return j


print(uncompress('2c3a1t'))
