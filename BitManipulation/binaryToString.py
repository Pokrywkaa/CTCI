def binaryToString(num):
    result='.'
    if num < 0 or num > 1:
        return 'ERROR'
    while num>0:
        if len(result)>32:
            return 'ERROR'
        r=num*2
        if r>=1:
            result+='1'
            num=r-1
        else:
            result+='0'
            num=r
    return result

if __name__=='__main__':
    print(binaryToString(0.625))
    print(binaryToString(1.75))
    print(binaryToString(0.33))
    print(binaryToString(0.25))
