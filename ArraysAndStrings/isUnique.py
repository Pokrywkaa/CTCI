def isUnique(s):
    hash={}
    for i in s:
        x=hash.get(i)
        if x:
            return False
        else:
            hash[i]=True
    return True

print(isUnique('ABCDE'))
print(isUnique('ABCDEA'))
