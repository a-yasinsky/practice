def reverse_recursion(s):
    print(s)
    if len(s) == 0:
        return []
    else:
        return [s.pop()] + reverse_recursion(s)

def reverseString(s):
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    if len(s) < 2:
        return s
    start = 0
    last = len(s) - 1
    while start < last:
        s[start],s[last] = s[last],s[start]
        start += 1
        last -= 1
    return s

print(reverseString(["H","a","n","n","a","h"]))
print(reverse_recursion(["h","e","l","l","o"]))
