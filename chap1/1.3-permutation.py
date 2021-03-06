def isPermutation(str1, str2):
    return sorted(str1) == sorted(str2)

print(isPermutation("apple","papel"))
print(isPermutation("apple","papeh"))

def check_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    counter = [0] * 256 # ASCII
    for c in str1:
        counter[c] += 1
    for c in str2:
        if counter[c] == 0:
            return False
        counter[c] -= 1
    return True
