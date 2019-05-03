def primePalindrome(N):
    """
    :type N: int
    :rtype: int
    """
    if N < 1 :
        return 1
    num = N
    while not (isPrime(num) and isPalindrom(num)):
        num += 1
    return num

def isPrime(num):
    if num < 2:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0 :
            return False
        i += 1
    return True

def isPalindrom(num):
    strNum = str(num)
    return strNum == strNum[::-1]

print(primePalindrome(-3))
