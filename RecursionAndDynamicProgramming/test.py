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


def grid(row, col):
    path = []
    grid_path(row-1, col-1, path)
    return path

def grid_path(n,m,path):
    if n < 0 or m < 0:
        return False
    
    isAtOrigin = n == 0 and m == 0
    
    if isAtOrigin or grid_path(n, m-1, path) or grid_path(n-1, m, path):
        path.append((n,m))
        return True

print(grid(3,3))