#Fall2019W7
#B-Coins and Triangle

def main():
    ntests = int(input())
    lstCoins = []
    for i in range(ntests):
        lstCoins.append(int(input()))
    for i in range(ntests):
        nCoins = lstCoins[i]
        rowLen = 1
        height = 0
        while (nCoins - rowLen >= 0):
            nCoins -= rowLen
            height += 1
            rowLen += 1
        print(height)

main()
#revise solution
#use summation formula
#use binary search method to look for n, when N is large
