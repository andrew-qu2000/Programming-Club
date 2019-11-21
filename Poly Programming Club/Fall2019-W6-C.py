#Aggressive Cows

def bestMinDif(cows, stalls): #n cows, list of stalls
    if cows == 2:
        return stalls[-1] - stalls[0]
    return 0

def main():
    stalls = [1,2,3,4,5,6,7]
    print(bestMinDif(2,stalls[0:5]))
    print(bestMinDif(2,stalls[2:6]))
    print(bestMinDif(2,stalls[1:4]))
