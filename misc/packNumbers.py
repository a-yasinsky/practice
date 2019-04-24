def packNumbers(arr):
    valMap = {x:0 for x in arr}
    for val in arr:
        valMap[val] += 1
    retList = ["{}:{}".format(key,valMap[key]) if valMap[key] > 1 else key for key in valMap]
    return retList

print(packNumbers([8,5,5,5,7,7,3,4,7]))
