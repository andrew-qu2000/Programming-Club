#Fall2019W13A

def playGame(cards, start, end):
    sereja, dima = 0, 0
    serejasTurn = True
    while(start <= end):
        if(cards[start] > cards[end]):
            if(serejasTurn):
                sereja += cards[start]
            else:
                dima += cards[start]
            start += 1
        else:
            if(serejasTurn):
                sereja += cards[end]
            else:
                dima += cards[end]
            end -= 1
        serejasTurn = not serejasTurn
    print(str(sereja)+' '+str(dima))
    
def main():
    ncards = int(input())
    cardLst = input().split()
    cardLst = [int(k) for k in cardLst]
    playGame(cardLst,0,ncards-1)
    
main()
