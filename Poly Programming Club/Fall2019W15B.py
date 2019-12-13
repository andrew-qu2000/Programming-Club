#Fall2019W15B

def main():
    nTests = int(input())
    outputs = []
    x,y = 0,0
    for i in range(nTests):
        xandy = [int(k) for k in input().split()]
        x = xandy[0]
        y = xandy[1]
        if (x - y > 1):
            outputs.append("YES")
        else:
            outputs.append("NO")
    for i in range(nTests):
        print(outputs[i])

main()
