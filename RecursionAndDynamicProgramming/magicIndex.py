#brute force
def magic_index(A):
    for index, val in enumerate(A):
        if index == val:
            return index
    return False

print(magic_index([2,6,10,3]))

#recursive
def magic_index2(A):
    return is_magic(A, 0, len(A)-1)

def is_magic(A, low, high):
    if high>=low:
        mid = (high + low) // 2
        if A[mid]==mid:
            return mid
        elif A[mid]>mid:
            return is_magic(A, low, mid-1)
        else:
            return is_magic(A, mid+1, high)

def magic_index3(A):
    return is_magic2(A, 0, len(A)-1)

def is_magic2(A, low, high):
    if high>=low:
        mid = (low+high)//2
        if mid==A[mid]:
            return mid

        #left search
        leftIndex = min(mid-1, A[mid])
        left = is_magic2(A, low, leftIndex)
        if left:
            return left

        #right search
        rightIndex = max(mid+1, A[mid])
        right = is_magic2(A, rightIndex, high)
        return right
    
print(magic_index3([-10,-5,2,2,2,3,4,7,9,12,13]))
print(magic_index3([-10,-2,0,3,10]))