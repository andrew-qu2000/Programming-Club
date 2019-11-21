#Fall2019W7
#C-Elevator Trouble

def failMsg():
    print("use the stairs")
    
def main():
    params = input().split()
    f = int(params[0])
    s = int(params[1])
    g = int(params[2])
    u = int(params[3])
    d = int(params[4])
    floorDif = g - s
    curr = s
    buttonPresses = 0
    if (floorDif % 2 == 1 and u % 2 == 0 and d % 2 == 0):
        failMsg()
    #incomplete
            
#use breadth first search
#queues or dictionaries??
