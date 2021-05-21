"""Binary search & variations"""


def bisect(arr, x):
	"""Binary search (only true) arr = [o, ..., o, x, o, ..., o].
                                                   ^
	"""
	lo, hi = 0, len(arr)-1 # left close & right close 
	while lo <= hi: 
		mid = lo + hi >> 1
		if arr[mid] == x: return mid
		if arr[mid] < x: lo = mid + 1 
		else: hi = mid - 1
	return -1 


def bisect_left(arr, x): 
	"""Binary search array to find (left-most) x."""
	lo, hi = 0, len(arr)               # detail 1: len(arr) vs len(arr) - 1
	while lo < hi:                     # detail 2: lo < hi vs lo <= hi
		mid = lo + hi >> 1             # detail 3: lo + hi >> 1 vs lo + hi + 1 >> 1
		if arr[mid] < x: lo = mid + 1  # detail 4: arr[mid] < x vs arr[mid] <= x
		else: hi = mid                 # detail 5: lo = mid + 1 & hi = mid vs lo = mid & hi = mid - 1
	return lo 


def bisect_right(arr, x): 
	"""Binary search array to find (right-most) x."""
	lo, hi = 0, len(arr) # left close & right open 
	while lo < hi: 
		mid = lo + hi >> 1
		if arr[mid] <= x: lo = mid + 1 # notice "<="
		else: hi = mid 
	return lo


def bisect_true_first(arr): 
	"""Binary search (first True) arr = [0, ..., 0, 1, ..., 1].
	                                                ^
    """
	lo, hi = 0, len(arr)
	while lo < hi: 
		mid = lo + hi >> 1
		if arr[mid]: hi = mid
		else: lo = mid + 1
	return lo 


def bisect_true_last(arr): 
	"""Binary search (last True) arr = [1, ..., 1, 0, ..., 0].
	                                            ^
	"""
	lo, hi = -1, len(arr)-1 # left open & right close 
	while lo < hi: 
		mid = lo + hi + 1 >> 1
		if arr[mid]: lo = mid 
		else: hi = mid - 1
	return lo  


if __name__ == "__main__": 
	arr = [1,1,2,2,2,2,2,2,3,3]
	print(bisect_left(arr, 2)) # expect 2
	print(bisect_right(arr, 2)) # expect 8

	print(bisect_true_first([0,0,0,1,1,1,1])) # expect 3
	print(bisect_true_last([1,1,1,1,0,0,0])) # expect 3