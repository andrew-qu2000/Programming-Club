#B - Cloning Toys

def main():
    inputs = input().split()
    copiesAim = int(inputs[0])
    originalsAim = int(inputs[1])
    runsOnOriginals = originalsAim - 1
    if runsOnOriginals == 0 and copiesAim > 0:
        print("No")
    elif (copiesAim - runsOnOriginals) < 0:
        print("No")
    elif (copiesAim - runsOnOriginals) % 2 == 0:
        print("Yes")
    else:
        print("No")

main()
