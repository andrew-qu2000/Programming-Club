#programming club 1 october 2019

#delete from the left

def matchStrings(s, t):
    indFromBack = 0
    sLast = len(s) - 1
    tLast = len(t) - 1
    cap = min(sLast,tLast)
    while (cap - indFromBack) >= 0 and s[sLast-indFromBack] == t[tLast-indFromBack]:
        indFromBack += 1
    print( len(s) + len(t) - 2*indFromBack )

def main():
    strS = input()
    strT = input()
    matchStrings(strS, strT)
    
main()
    
#matchStrings('test','west')
#matchStrings('codeforces','yes')
#matchStrings('test','yes')
#matchStrings('b','ab')
