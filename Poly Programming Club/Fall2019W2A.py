#Fall2019W2A
#Stock Arbitraging-Codeforces 1150A

if __name__ == "__main__":
    nmr = input().split()
    n = int(nmr[0])
    m = int(nmr[1])
    r = int(nmr[2])
    s = [int(k) for k in input().split()]
    b = [int(k) for k in input().split()]

    lowS = min(s)
    highB = max(b)

    if highB > lowS:
        stocksBought = r // lowS
        profit = (highB - lowS) * stocksBought
        print(r + profit)
    else:
        print(r)

    
