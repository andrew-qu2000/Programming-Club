#Fall2019W13B

def binSearchDorms(roomNum, directory):
    start, end = 0, len(directory) - 1
    i = len(directory) // 2
    while end - start >= 1:
        if roomNum < directory[i]:
            end = i
        elif roomNum > directory[i]:
            start = i
        else:
            return i
        i = (start + end) // 2
    return end
def main():
    nm = input().split()
    ndorms = nm[0]
    mletters = nm[1]
    rooms = [int(r) for r in input().split()]
    letters = [int(l) for l in input().split()]
    directory= [0 for i in range (int(ndorms))]
    directory[0] = 0
    #directory[0] = rooms[0]
    for i in range(int(ndorms)):
        directory.append(directory[i] + rooms[i])
    print(directory)
    for letter in letters:
        print(binSearchDorms(letter,directory))
    #for letter in letters:
     #   roomNum = letter
      #  rightDorm = 1
       # while letter > directory[rightDorm-1]:
        #    rightDorm += 1
        #if rightDorm > 1:
         #   roomNum -= directory[rightDorm - 2]
        #print(rightDorm, roomNum)
        
main()
