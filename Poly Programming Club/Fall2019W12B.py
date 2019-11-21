#Fall2019W12B

def numDecodes(encoding, oneChar):
    if encoding == '':
        return 1
    elif encoding == '0':
        return 0
    elif len(encoding) == 1:
        return 1
    elif len(encoding) == 2 and oneChar:
        if encoding[0] == '0':
            return 0
        elif int(encoding) > 26:
            return 0
        else:
            return 1
    else:
        return numDecodes(encoding[0], True)*numDecodes(encoding[1:], False) + numDecodes(encoding[:2], True)*numDecodes(encoding[2:], False)
    #EDIT: slicing is too slow
def main():
    inputs = []
    encoding = input()
    while encoding != '0':
        inputs.append(encoding)
        encoding = input()
    for inp in inputs:
        print(numDecodes(inp, False))
        
main()
