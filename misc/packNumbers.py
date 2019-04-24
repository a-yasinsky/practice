def packNumbers(arr):
    valMap = {x:0 for x in arr}
    for val in arr:
        valMap[val] += 1
    retList = []
    for key in valMap:
        if valMap[key] > 1:
            retList.append("{}:{}".format(key,valMap[key]))
        else:
            retList.append(key)
    return retList

print(packNumbers([8,5,5,5,7,7,3,4,7]))
