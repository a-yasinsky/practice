def findNumber(n):
    if '4' not in str(n) and '13' not in str(n):
        return n
    return findNumber(n+1)

def getLuckyFloorNumber(n):
    fList = []
    lastLucky = 0
    for i in range(n + 1):
        luckyNumber = findNumber(lastLucky)
        fList.append(luckyNumber)
        lastLucky = luckyNumber + 1
    return fList[n]

print(getLuckyFloorNumber(12))
