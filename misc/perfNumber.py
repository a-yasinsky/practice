def checkPerfectNumber(num):
    """
    :type num: int
    :rtype: bool
    """
    if num <= 0:
        return False
    i = 1
    sum = 0
    while i*i <= num:
        if num % i == 0:
            if i != num/i:
                sum += i + num/i
            else:
                sum += i
        i += 1
    return sum - num == num

print(checkPerfectNumber(28))
