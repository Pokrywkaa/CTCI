def lenOfBin(num):
    if ~num == 0:
        return False
    
    currentLength = 0
    previousLength = 0
    maxLength = 1

    while num != 0:
        if num & 1 == 1:
            currentLength+=1
        elif num & 1 ==0:
            if num & 2 == 0:
                previousLength=0
            else:
                previousLength=currentLength
            currentLength = 0
        maxLength = max(maxLength, currentLength + previousLength +1)
        num>>=1
        x=bin(num)
    return maxLength

if __name__ == '__main__':
    print(lenOfBin(1775))