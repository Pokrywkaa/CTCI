import time

def fibo(n):
    if n == 0: return 0
    if n==1: return 1
    return fibo(n-1) + fibo(n-2)

def fibo2(n, memo):
    if not n in memo:
        memo[n] = fibo2(n-2, memo) + fibo2(n-2, memo)
    return memo[n]

def fibo_memo(n):
    memo = {0:1, 1:1}
    return fibo2(n, memo)
start_time = time.time()
print(fibo(30))
print("---%s seconds ---" % (time.time()-start_time))
start_time = time.time()
print(fibo_memo(30))
print("---%s seconds ---" % (time.time()-start_time))