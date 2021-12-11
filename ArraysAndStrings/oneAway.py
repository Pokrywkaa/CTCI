def oneAway(s1, s2):
    
    if len(s1)-len(s2)>1:
        return False

    hash={}

    for i in s1:
        if not hash.get(i):
            hash[i]=1
        else:
            hash[i]+=1

    if len(s1)!=len(s2):
        change=True
    else:
        change=False

    for i in s2:
        x=hash.get(i)
        if not x:
            if change:
                return False
            change=True
        elif x==1:
            hash[i]=0
        else:
            hash[i]-=1
    return True

print(oneAway('pales', 'pale'))