def highestValuePalindrome(n,k,s):
    for i in range(n//2):
        print(s[i], s[n-1-i])
        if s[i] != s[n-1-i]:
            if k > 0:
                s = s[:i] + '9' + s[i+1:n-i-1] + '9' + s[n-i:]
                k -= 1
            else:
                return -1
    return s


n = 6
k = 3
s = "092282"
print(highestValuePalindrome(n,k,s))
