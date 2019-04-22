def findMedian(values):
    sortedValues = sorted(values)
    def find(newVal = None):
        if newVal:
            sortedValues.append(0)
            pos = len(sortedValues) - 1
            while pos > 0 and sortedValues[pos-1] > newVal:
                 sortedValues[pos] = sortedValues[pos-1]
                 pos -= 1
            sortedValues[pos]=newVal
        med = len(sortedValues) // 2
        rval = sortedValues[med]
        sortedValues.pop(0)
        return rval
    return find

def activeNotifications(n,d,values):
    notif = 0
    find = findMedian(values[:d])
    for i in range(d + 1,n):
        med = find(values[i-1])
        if values[i]*2 >= med:
            notif += 1
    return notif

n = 9
d = 5
values = [2,3,4,2,3,6,8,4,5]
print(activeNotifications(n,d,values))
