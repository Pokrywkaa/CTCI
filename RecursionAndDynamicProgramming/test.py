# import time

# def fibo(n):
#     if n == 0: return 0
#     if n==1: return 1
#     return fibo(n-1) + fibo(n-2)

# def fibo2(n, memo):
#     if not n in memo:
#         memo[n] = fibo2(n-2, memo) + fibo2(n-2, memo)
#     return memo[n]

# def fibo_memo(n):
#     memo = {0:1, 1:1}
#     return fibo2(n, memo)
# start_time = time.time()
# print(fibo(30))
# print("---%s seconds ---" % (time.time()-start_time))
# start_time = time.time()
# print(fibo_memo(30))
# print("---%s seconds ---" % (time.time()-start_time))
def tripleStep(n):
    if n<0:
        return 0
    if n == 0:
        return 1
    return(tripleStep(n-1)+tripleStep(n-2)+tripleStep(n-3))
print(tripleStep(3))

def fibo(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibo(n-1)+fibo(n-2)

def fibo2(n):
    return fibo2_helper(n, {0:0,1:1})

def fibo2_helper(n, memo):
    if not n in memo:
        memo[n] = fibo2_helper(n-2, memo)+fibo2_helper(n-1, memo)
    return memo[n]

def valid_parens(s):
    valid = {'{': '}', '(': ')', '[': ']'}
    stack = []
    for i in s:
        if i in valid.keys():
            stack.append(valid[i])
        elif len(stack) != 0 and i == stack[-1]:
            stack.pop()
        elif i not in valid.keys() and i not in valid.values():
            continue
        else:
            return False
    if len(stack)==0:
        return True
    return False

print(valid_parens('{()}'))
            


