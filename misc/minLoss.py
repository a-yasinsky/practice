def findMinLoss(n,prices):
    counts = [x for x in range(len(prices))]
    zipPrices = zip(prices,counts)
    zipPrices = sorted(zipPrices, key = lambda x:x[0])
    zipPrices = zip(zipPrices[:], zipPrices[1:])
    valid = [(x1,x2) for x1,x2 in zipPrices if x1[1]>x2[1]]
    dist = [x2[0] - x1[0] for x1,x2 in valid]
    return min(dist)

n = 5
prices = [20,15,8,2,12]
print(findMinLoss(n,prices))
