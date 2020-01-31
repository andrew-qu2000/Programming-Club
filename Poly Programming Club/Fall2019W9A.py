#Fall2019W9A
#Yet Another Dividing Into Teams | Codeforces 1249A

if __name__ == "__main__":
    nqueries = int(input())
    outputs = []
    for query in range(nqueries):
        nstudents = int(input())
        skills = [int(k) for k in input().split()]
        skills.sort()
        twoTeams = False
        ind = 0
        while (not twoTeams) and ind < nstudents - 1:
            if abs( skills[ind] - skills[ind+1] ) == 1:
                twoTeams = True
            ind += 1
        if twoTeams:
            outputs.append(2)
        else:
            outputs.append(1)
    for o in outputs:
        print(o)
