#Fall2019W7
#A-Polycarp's Pockets

def main():
    ncoins = int(input())
    arr = input().split()
    values = [int(k) for k in arr]
    values.sort()
    npockets = 1
    ind = 0
    while(ind < ncoins):
        count = 1
        curr = values[ind]
        while(ind+count < ncoins and values[ind+count]==curr):
            count += 1
        npockets = max(npockets,count)
        ind += 1
    print(npockets)

main()
