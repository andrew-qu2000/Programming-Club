#Fall2019W11A
#Ania and Minimizing | Codeforces 1230B

if __name__ == "__main__":
    nandk = input().split()
    inNum = input()
    nDigits = int(nandk[0])
    kMaxChanges = int(nandk[1])
    digitLst = [int(d) for d in inNum]
    ind = 0
    changes = 0
    while ind < nDigits and changes < kMaxChanges:
        if ind == 0:
            if nDigits == 1:
                digitLst[ind] = 0
                changes += 1
            elif digitLst[ind] != 1:
                digitLst[ind] = 1
                changes += 1
        else:
            if digitLst[ind] != 0:
                digitLst[ind] = 0
                changes += 1
        ind += 1
    outNumStr = ""
    for digit in digitLst:
        outNumStr += str(digit)
    print(int(outNumStr))
#revise
