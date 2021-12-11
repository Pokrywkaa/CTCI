def compression(s):
    hash={}
    new_str=''
    for i in s:
        if not hash.get(i):
            hash[i]=1
        else:
            hash[i]+=1
    for key, value in hash.items():
        new_str+=str(key)+str(value)
    if len(new_str)>len(s):
        return s
    return new_str
print(compression('aaaabbbccdd'))
print(compression('abcd'))