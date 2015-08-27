def isPermutation(s1, s2):
    dic = {}
    for c in s1:
        try:
            dic[c] += 1
        except KeyError:
            dic[c] = 1
    for c in s2:
        try:
            dic[c] -= 1
        except KeyError:
            return False

    return all(e == 0 for e in dic.values())

def isPermutation2（s1, s2):
    return sorted(s1) == sorted(s2)

print isPermutation("af","f4")
print isPermutation("12343","33124")
