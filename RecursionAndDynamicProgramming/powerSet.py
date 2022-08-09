def powerSet(s):
    if len(s)==0:
        return [[]]
    else:
        res = []
        for subset in powerSet(s[1:]):
            res += [subset]
            res += [[s[0]]+subset]
        return res

print(powerSet([0,1,2]))