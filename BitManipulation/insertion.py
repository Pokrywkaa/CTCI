def getBit(M, i):
    if int(M,2) & (1<<i):
        return 1
    return 0

def updateBit(N, value, i):
    N = int(N,2) & ~(1<<i)
    N = N|(value<<i)
    return bin(N)

def insertion(N, M, i, j):
    for bit in range(j-i+1):
        val=getBit(M, bit)
        N = updateBit(N, val, i+bit)
    return N

def insertion2(N, M, i, j):
    allOnes = ~0
    left = allOnes<<(j+1)
    right = ((1<<i)-1)
    mask = left | right
    N_cleared = int(N,2) & mask
    M_shifted = int(M,2) << i
    return bin(N_cleared | M_shifted)

if __name__=='__main__':
    print(insertion('10000000000', '10011', 2, 6))
    print(insertion2('10000000000', '10011', 2, 6))
