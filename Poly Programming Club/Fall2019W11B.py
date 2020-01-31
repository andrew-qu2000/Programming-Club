#Fall2019W11B
#Dawid and Bags of Candies | Codeforces 1230A

if __name__ == "__main__":
    bags = [int(k) for k in input().split()]
    bags.sort()
    if bags[3] == sum(bags[:3]):
        print("YES")
    elif bags[0] + bags[3] == bags[1] + bags[2]:
        print("YES")
    else:
        print("NO")
    
