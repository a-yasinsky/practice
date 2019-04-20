PI = 3.14

def devideCake(cakes, guests):
    cakes.sort()
    cakesSqr = list(map(lambda x : x**2*PI, cakes))
    maxSqr = cakesSqr[len(cakesSqr) - 1]
    return findPiece(cakesSqr, guests, 0, maxSqr)

def findPiece(cakes, guests, minSqr, maxSqr):
    midSqr = (minSqr + maxSqr) / 2
    pieses = countPieces(cakes, midSqr)
    if pieses == guests :
        return midSqr
    elif pieses > guests:
        return findPiece(cakes, guests, midSqr, maxSqr)
    else:
        return findPiece(cakes, guests, minSqr, midSqr)


def countPieces(cakes, sqr):
    sum = 0
    for cake in cakes:
        sum += cake // sqr
    return sum

cakes = [1,1,1,2,3]
guests = 6
print(devideCake(cakes,guests))
