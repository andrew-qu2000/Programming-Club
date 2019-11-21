#A-Turn the Rectangles

def main():
    nRects = int(input())
    rects = []
    for i in range(nRects):
        dimensions = input().split()
        rects.append( ( int(dimensions[0]),int(dimensions[1]) ) )
    #print(rects)
    prevHeight = -1
    for rect in rects:
        mx = max(rect[0],rect[1])
        mn = min(rect[0],rect[1])
        if prevHeight < 0:
            prevHeight = mx
        elif mx > prevHeight:
            if mn <= prevHeight:
                prevHeight = mn
            else:
                print("NO")
                return
        else:
            prevHeight = mx
    print("YES")
            
main()
