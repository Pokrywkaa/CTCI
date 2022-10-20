# Solution 1

def min_product(a,b):
    bigger = a if a > b else b
    smaller = a if a < b else b
    return min_product_helper(smaller, bigger)

def min_product_helper(smaller, bigger):
    if smaller == 0:
       return 0
    elif smaller == 1:
        return bigger
    s = smaller>>1
    side1 = min_product_helper(s, bigger)
    side2 = side1
    if smaller % 2 == 1:
        side2 = min_product_helper(smaller-s, bigger)
    return side1+side2    

# Solution 2 

def min_product2(a,b):
    bigger = a if a > b else b
    smaller = a if a < b else b
    return min_product_helper2(smaller, bigger, {})

def min_product_helper2(smaller, bigger, memo):
    if smaller == 0:
       return 0
    elif smaller == 1:
        return bigger
    elif smaller in memo:
        return memo[smaller]
    s = smaller>>1
    side1 = min_product_helper2(s, bigger, memo)
    side2 = side1
    if smaller % 2 == 1:
        side2 = min_product_helper2(smaller-s, bigger, memo)
    memo[smaller]=side1+side2
    return memo[smaller] 

# Solution 3

def min_product3(a,b):
    bigger = a if a > b else b
    smaller = a if a < b else b
    return min_product_helper3(smaller, bigger)

def min_product_helper3(smaller, bigger):
    if smaller == 0:
       return 0
    elif smaller == 1:
        return bigger
    s = smaller>>1
    halfProd = min_product_helper3(s, bigger)
    if smaller % 2 == 0:
        return halfProd + halfProd
    else:
        return halfProd + halfProd + bigger


import time

start_time = time.time()
print(min_product(171231231,231231231))
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
print(min_product2(171231231,231231231))
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
print(min_product3(171231231,231231231))
print("--- %s seconds ---" % (time.time() - start_time))