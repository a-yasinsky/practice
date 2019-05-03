import math
def checkPerfectNumber(num):
    """
    :type num: int
    :rtype: bool
    """
    i = 1
    divisors = []
    while i <= math.sqrt(num):
        if num % i == 0:
            if i != num/i and num/i != num:
                divisors += [i, num/i]
            else:
                divisors.append(i)
        i += 1
    return sum(divisors) == num

print(checkPerfectNumber(28))
