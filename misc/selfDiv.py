def selfDividingNumbers(left, right):
    """
    :type left: int
    :type right: int
    :rtype: List[int]
    """
    retList = []
    for num in range(left,right+1):
        numStr = str(num)
        if "0" in numStr:
            continue
        selfDiv = True
        for let in numStr:
            letNum = int(let)
            if num % letNum != 0:
                selfDiv = False
                break
        if selfDiv:
            retList.append(num)

    return retList

print(selfDividingNumbers(1,22))
