def maxProfitN(prices):
    diffs = [0] * (len(prices) - 1)
    for x in range(len(prices) - 1):
        diffs[x] = prices[x+1] - prices[x]
    maxDif = diffs[0]
    for i in range(1,len(diffs)):
        if diffs[i-1] > 0:
            diffs[i] += diffs[i-1]
        maxDif = max(maxDif,diffs[i])
    return maxDif


def maxProfit1(prices):
    dif = prices[1]-prices[0]
    curSum = dif
    maxSum = curSum
    for x in range(1, len(prices)-1):
        locDif = prices[x+1] - prices[x]
        if curSum > 0:
            curSum += locDif
        else:
            curSum = locDif
        maxSum = max(maxSum, curSum)
    return maxSum

print(maxProfitN([3,3,5,0,0,3,1,4]))
print(maxProfit1([3,3,5,0,0,3,1,4]))
