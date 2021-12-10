def permutation(s1, s2):

    if len(s1) != len(s2):
        return False

    hash={}

    for i in s1:
        if hash.get(i):
            hash[i]+=1
        else:
            hash[i]=1

    for i in s2:
        x=hash.get(i)
        if not x:
            return False
        elif x==1:
            hash[i]=0
        else:
            hash[i]-=1
    
    return True

print(permutation('AB CD', 'ADBC '))
print(permutation('ABC', 'CAN'))
