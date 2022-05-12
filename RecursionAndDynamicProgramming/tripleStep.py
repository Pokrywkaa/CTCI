def step(n):
    if n<0:
        return 0
    elif n==0:
        return 1
    else:
        return step(n-1)+step(n-2)+step(n-3)

def step2(n):
    memo = [-1]*(n+1)
    return countWays(n, memo)

def countWays(n, memo):
    if n<0:
        return 0
    elif n==0:
        return 1
    elif memo[n]>-1:
        return memo[n]
    else:
        memo[n] = countWays(n-1, memo) + countWays(n-2, memo) + countWays(n-3, memo)
        return memo[n]
print(step(3))
print(step2(3))
