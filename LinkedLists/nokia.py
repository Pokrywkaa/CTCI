def solution(s):
    count=0
    smallest=s[0]
    for i in s[1:]:
        if smallest>=i:
            count+=1
            smallest=i
    return count
            
        

print(solution('damian'))



