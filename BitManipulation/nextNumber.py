def nextNumber(num):
    c = num
    c0 = 0
    c1 = 0

    while c&1 == 0 and c != 0:
        c0+=1
        c>>=1

    while c&1 == 1:
        c1+=1
        c>>=1

    p = c0+c1
    num |= (1<<p)
    num &= ~((1<<p)-1)
    num |= (1<<(c1-1))-1

    return num 


def prevNumber(num):
    c = num
    c0 = 0
    c1 = 0
    
    while c&1==1:
        c1+=1
        c>>=1
    while c&1==0 and c!=0:
        c0+=1
        c>>=1

    p = c0+c1
    num &= ~0 << p+1
    mask = (1 << (c1+1))-1
    num |= mask << c0-1
    
    return num

if __name__=='__main__':
    print(nextNumber(13948))
    print(prevNumber(13948))