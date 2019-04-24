def packNumbers(arr):
    retArr = []
    last = 0
    count = 1
    for k,val in enumerate(arr):
        if k == 0:
            last = val
            continue
        if val == last:
            count += 1
        else:
            retArr.append("{}:{}".format(last,count) if count>1 else last)
            count = 1
            last = val
    retArr.append("{}:{}".format(last,count) if count>1 else last)
    return retArr

print(packNumbers([8,5,5,5,7,7,3,4,7,6,6]))
