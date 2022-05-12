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
    
print(magic_index2([-10,-2,0,3,10]))