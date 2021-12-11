def palindromePermutation(s):
    hash={}
    for i in s:
        if i!=' ':
            if not hash.get(i):
                hash[i]=1
            else:
                hash[i]+=1
    foundOdd=False
    for key in hash:
        if hash[key]%2==1:
            if foundOdd:
                return False
            foundOdd=True
    return True
print(palindromePermutation('tact coa'))