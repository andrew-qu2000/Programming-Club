def relativelyPrimePairs(left, right):
    curr = left;
    print("YES")
    while curr < right:
        print( curr, curr+1 )
        curr += 2

if __name__ == "__main__":
    x, y = [int(inp) for inp in input().split()]
    relativelyPrimePairs(x, y)
