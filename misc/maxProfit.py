def maxProfit(prices):
    count = [x for x in range(len(prices))]
    zipPrices = zip(prices,count)
    zipPrices = sorted(zipPrices, key = lambda x:x[0])
    maxDiff = 0
    ln = len(zipPrices)
    for i in range(ln):
        if zipPrices[ln - 1 - i][1] > zipPrices[0][1]:
            maxDiff = zipPrices[len(zipPrices) -1 - i][0] - zipPrices[i][0]
            break
    return list(zipPrices), maxDiff

print(maxProfit([3,3,5,0,0,3,1,4]))
