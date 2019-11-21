#Fall2019-W12A - Maximum Square

def maxSquare(nPlanks, pLengths):
    sortedLengths = sorted(pLengths)
    longest = max(pLengths)
    for length in range(longest,0,-1):
        count = 0
        ind = len(sortedLengths) - 1
        while ind >= 0 and (sortedLengths[ind] >= length):
            count += 1
            ind -= 1
        if count >= length:
            return length
        count = 0
        #EDIT: instead of counting, just go 'length' steps back and check the value there
    return 1
    
def main():
    numTrials = int(input())
    numPlanks = 0
    plankLengths = []
    outputs = []
    for trial in range(numTrials):
        numPlanks = int(input())
        plankLengths = input().split()
        plankLengths = [int(plankLengths[i]) for i in range(numPlanks)]
        outputs.append(maxSquare(numPlanks,plankLengths))
    for ans in outputs:
        print(ans)
main()
