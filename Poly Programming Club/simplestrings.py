#simple strings

def compactify(inString):
    retList = []
    currChar = "A"
    chainLen = 0
    for i in range(len(inString)):
        if inString[i] == currChar:
            chainLen += 1
        else:
            if chainLen > 0:
                retList.append( (currChar, chainLen) )
            currChar = inString[i]
            chainLen = 1
    retList.append( (currChar, chainLen) )
    print(retList)
            
        
