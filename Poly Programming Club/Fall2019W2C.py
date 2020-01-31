#Fall2019W2C
#Make Product Equal One | CodeForces 1206B

if __name__ == "__main__":
    listLen = int(input())
    factors = [int(k) for k in input().split()]
    negCount,currFactor,ind,cost = 0,0,0,0
    zeroFound = False
    while ind < listLen:
        currFactor = factors[ind]
        if currFactor == 0:
            zeroFound = True
            cost += 1 #turn 0 into 1
        elif currFactor > 0:
            cost += (currFactor - 1) #turn factor into 1
        else:
            cost += (abs(currFactor) - 1) #turn factor into -1
            negCount += 1 #increment count of neg factors
        ind += 1
    if negCount % 2 == 0 or zeroFound:
        print(cost)
    else:
        print(cost + 2)
