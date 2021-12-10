def urlify(s, l):
    result=''
    for i in range(l):
        if s[i]==' ':
            result+='%20'
        else:
            result+=s[i]
    return result

print(urlify('test test    ', 9))

def urlify2(s, l):
    s=list(s)

    len_str=0

    for i in range(l):
        if s[i]==' ':
            len_str+=3
        else:
            len_str+=1
    for i in reversed(range(l)):
        if s[i]==' ':
            s[len_str-3:len_str]='%20'
            len_str-=3
        else:
            s[len_str-1]=s[i]
            len_str-=1
    toStr=''.join(str(x) for x in s)
    return toStr

print(urlify2('test test              ',9))



