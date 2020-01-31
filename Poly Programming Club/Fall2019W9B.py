#Fall2019W9B
#Broken Keyboard | CodeForces 1251A

if __name__ == "__main__":
    nqueries = int(input())
    outputs = []
    for q in range(nqueries):
        testStr = input()
        strLen = len(testStr)
        res = ""
        ind = 0
        while ind < strLen:
            currChar = testStr[ind]
            if ind + 1 < strLen:
                if currChar == testStr[ind + 1]:
                    ind += 1
                else:
                    if currChar not in res:
                        res += currChar
            else:
                if currChar not in res:
                    res += currChar
            ind += 1
        sortedResLst = sorted(res)
        res = ""
        for char in sortedResLst:
            res += char
        outputs.append(res)
    for o in outputs:
        print(o)
