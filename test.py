#============================================================================#
# subsets
#============================================================================#

def subsets(array):
    """iterative solution"""
    n = len(array)
    subsets_ = []

    for i in range(1<<n):
        subsets_.append([array[j] for j in range(n) if i & (1<<j)])
    return subsets_

#print(subsets([1,2,3,4,5,6,7,8,9]))

def subsets(array, curr=0, subset=[]):
    """tail recursion"""
    if curr == len(array):
        subsets_.append(subset)
        return
    subsets(array, curr+1, subset)
    subsets(array, curr+1, subset.append(array[start]))


def gcd(n, k):
    while k:
        n, k = k, n%k
    return n


def palin_substrings(string):
    """"""
    count = 0
    for center in range(2*len(string)-1):
        left, right = center//2, (center+1)//2
        while left >= 0 and right < len(string) and string[left] == string[right]:
            count += 1
            left -= 1
            right += 1
    return count 

def sum_unique(array):
    """"""
    prev, sum = array[0], array[0]
    for i in range(len(array)):
        if array[i] <= prev:
            prev += 1
        else:
            prev = array[i]
        sum += prev
    return sum 

def mindiff(array):
    """"""
    array.sort()
    return min([array[i] - array[i-1] for i in range(1, len(array))])

def power(x, n):
    """"""
    if x == 0: return 0

    if n < 0:
        x, n = 1/x, -n

    temp = power(x, n//2)
    if n % 2:
        return temp * temp * x
    else:
        return temp * temp 

def zig_sort(arr):
    """"""
    aux = sorted(arr)
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        arr