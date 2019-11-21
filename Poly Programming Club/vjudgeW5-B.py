def buggyRobot():
    xcor = 0
    ycor = 0
    numMoves = input()
    dirSeq = input()
    for direct in dirSeq:
        if direct == 'U':ycor += 1
        elif direct == 'D':ycor -= 1
        elif direct == 'L':xcor -= 1
        else:xcor += 1
    print( int(numMoves) - abs(xcor) - abs(ycor) )
            
buggyRobot()
