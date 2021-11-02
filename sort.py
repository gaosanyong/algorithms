"""SORTING ALGORITHMS
Any compare-based sorting algorithms must use at least log(N!) ~ NlogN 
compares in the worst-case

      algorithm | guarantee |  random  | space | stable
-------------------------------------------------------
 insertion sort |    N**2/2 |   N**2/4 | 1     | yes
    bubble sort |    N**2/2 |   N**2/2 | 1     | yes
      heap sort |     2NlgN |    2NlgN | 1     | no
     merge sort |      NlgN |     NlgN | N     | yes
     quick sort |  1.39NlgN | 1.39NlgN | clgN  | no
 selection sort |    N**2/2 |   N**2/2 | 1     | no
     shell sort |    ?      |   ?      | 1     | no
LSD string sort |       2NW |      2NW | N+R   | yes
MSD string sort |       2NW | NlogR(N) | N+DR  | yes	
3-way string    | 1.39WNlgN | 1.39NlgN | logN + W | no
quick sort      | 
-------------------------------------------------------
"""
from random import randint 

CUTOFF = 1 # cutoff to switch to insertion sort in merge sort

def shuffle(comparables, lo=0, hi=None):
	"""Randomly shuffle an array in place

	Arguments:
	comparables -- an array of which the elements can be compared
	lo          -- lower bound of indices (default 0)
	hi          -- higher bound of indices (default None)

	Knuth shuffle loops through an array. At each location i, a random 
	integer r between 0 and i (inclusive) is generated. Elements at r and i
	are swapped. 
	"""
	if hi is None:
		hi = len(comparables)

	for i in range(lo, hi):
		r = randint(lo, i)
		if i != r:
			comparables[r], comparables[i] = comparables[i], comparables[r]


def issorted(comparables, lo=0, hi=None):
	"""Return True if comparables is sorted in ascending order

	Arguments:
	comparables -- an array of which the elements can be compared
	lo          -- lower bound of indices (default 0)
	hi          -- higher bound of indices (default None)
	"""
	if hi is None:
		hi = len(comparables)

	for i in range(lo, hi-1):
		if comparables[i] > comparables[i+1]:
			return False
	return True


def bbsort(comparables, lo=0, hi=None):
	"""Bubble sort an array into ascending order in place

	Arguments:
	comparables -- an array of which the elements can be compared
	lo          -- lower bound of indices (default 0)
	hi          -- higher bound of indices (default None)

	Bubble sort loops through an array progressively, and swap adjacent pairs 
	that are in wrong order. 
	"""
	if hi is None:
		hi = len(comparables)

	for i in range(lo, hi):
	# ith largest item in place upon ith pass
		for j in range(lo, hi-i-1):
			if comparables[j] > comparables[j+1]:
				comparables[j], comparables[j+1] = comparables[j+1], comparables[j]


def slsort(comparables, lo=0, hi=None):
	"""Selection sort an array into ascending order in place

	Arguments:
	comparables -- an array of which the elements can be compared
	lo          -- lower bound of indices (default 0)
	hi          -- higher bound of indices (default None)

	Selection sort loops through an array progressively. On each pass, the 
	smallest element in remaining entries is swapped with the current one.
	"""
	if hi is None:
		hi = len(comparables)

	for i in range(lo, hi):
		m = i #minimum of remaining entries
		for j in range(i+1, hi):
			if comparables[j] < comparables[m]:
				m = j
		comparables[i], comparables[m] = comparables[m], comparables[i]


def insort(comparables, lo=0, hi=None):
	"""Insertion sort an array into ascending order in place

	Arguments:
	comparables -- an array of which the elements can be compared
	lo          -- lower bound of indices (default 0)
	hi          -- higher bound of indices (default None)

	Insertion sort loops through an array. At given position, the current 
	element is progressively swapped with previous elements that are in wrong 
	order to make sure that array up to current position is in correct order.
	"""
	if hi is None:
		hi = len(comparables)

	for i in range(lo, hi):
		for j in range(i, lo, -1):
			if comparables[j-1] <= comparables[j]: # "<=" key for stability
			#correct order
				break
			else: 
			# wrong order				
				comparables[j-1], comparables[j] = comparables[j], comparables[j-1]


def shsort(comparables, lo=0, hi=None):
	"""Shell sort an array into ascending order in place

	Arguments:
	comparables -- an array of which the elements can be compared
	lo          -- lower bound of indices (default 0)
	hi          -- higher bound of indices (default None)

	Shell sort h-sorts subarrays, and progressively decreases stride following 
	Knuth sequence.

	Ref: Shell (1959) A high-speed sorting procedure
	"""
	if hi is None:
		hi = len(comparables)

	h = 1 # stride 
	while h < (hi - lo) // 3:
		h = 3 * h + 1 # Knuth sequence: 1, 4, 13, 40, 121 ...

	while h >= 1: 
	#insertion sort with stride "h"
		for i in range(lo + h, hi):
			for j in range(i, lo + h-1, -h):
				if comparables[j] < comparables[j-h]:
					comparables[j-h], comparables[j] = comparables[j], comparables[j-h]
				else:
					break
		h = h // 3


def mgsort(comparables, bu=False):
	"""Merge sort an array into ascending order

	Arguments:
	comparables -- an array of which the elements can be compared
	bu          -- flag to turn on "bottom-up" approach (default False)

	Merge sort divides the array into two halves, sorts the two halves 
	respectively, and merges the two sorted halves into a sorted array. 

	When bu=True, bottom-up merge sort is used in which elements are 
	progressively merged into a sorted array without recursive calls. 
	"""
	if not bu:
	#regular merge sort
		auxiliary = comparables[:]
		_mgsort(comparables, auxiliary, 0, len(comparables))
	else:
	#bottom-up merge sort
		N = len(comparables)
		sz = 1
		while sz < N:
			auxiliary = comparables[:]
			for lo in range(0, N-sz, 2*sz):
				_merge(comparables, auxiliary, lo, lo+sz, min(lo+2*sz, N))
			sz *= 2	


def _mgsort(comparables, auxiliary, lo, hi):
	"""Merge sort helper function 

	Arguments:
	comparables -- an array of which the elements can be compared
	auxiliary   -- an auxiliary array for sorted sub-arrays
	lo          -- lower bound of indices
	hi          -- higher bound of indices
	"""

	# merge sort too heavy for tiny arrays
	# cutoff to insertion sort
	if hi - lo <= CUTOFF:
		insort(comparables, lo, hi)
		return

	mid = lo + (hi - lo)//2
	_mgsort(auxiliary, comparables, lo, mid)
	_mgsort(auxiliary, comparables, mid, hi)
	_merge(comparables, auxiliary, lo, mid, hi)


def _merge(comparables, auxiliary, lo, mid, hi):
	"""Merge two sorted halves into one sorted array in place

	Arguments:
	comparables -- (to) the destination array which is sorted after the merge
	auxiliary   -- (from) the origin array with two sorted halves
	lo          -- lower bound of indices
	mid         -- middle index to separate the two sorted halves
	hi          -- higher bound of indices	

	auxiliary[lo:mid] and auxiliary[mid:hi] are two sorted halves; 
	comparables[lo:hi] is a sorted array after merging.
	"""
	assert issorted(auxiliary[lo : mid])
	assert issorted(auxiliary[mid : hi])

	i, j = lo, mid
	for k in range(lo, hi):
		if i >= mid:
			comparables[k] = auxiliary[j]
			j += 1
		elif j >= hi:
			comparables[k] = auxiliary[i]
			i += 1
		elif auxiliary[i] <= auxiliary[j]: 
		# "<=" is essential for stability
			comparables[k] = auxiliary[i]
			i += 1
		else:
			comparables[k] = auxiliary[j]
			j += 1 
	assert issorted(comparables[lo : hi])


def qksort(comparables, dijk3=False):
	"""Quick sort an array into ascending order in place

	Arguments:
	comparables -- an array of which the elements can be compared

	Quick sort randomly shuffles the array to have a statistical guarantee of
	performance, partitions the array pivoting on the first element and sorts
	the two partitioned sub-arrays recursively until the array is sorted. 

	Hoare, C.A.R. (1961) Algorithm 64: Quicksort
	"""
	shuffle(comparables)
	if not dijk3:
		_qksort(comparables, 0, len(comparables))
	else:
		_qksort3(comparables, 0, len(comparables))


def _partition(comparables, lo, hi):
	"""Return index upon partitioning the array pivoting on the first element

	Arguments:
	comparables -- an array of which the elements can be compared
	lo          -- lower bound of indices
	hi          -- higher bound of indices

	After partition, 
	elements to the left of pivot are no larger than the pivot;
	elements to the right of pivot are no smaller than the pivot.

	comparables[lo:j] <= pivot
	comparables[j+1:hi] >= pivot

	This design choice is essential for Nlog(N) performance for 
	duplicate keys. 
	"""
	i = lo + 1
	j = hi - 1
	while i < j:
		while i < hi and comparables[i] < comparables[lo]: i += 1
		while j > lo and comparables[j] > comparables[lo]: j -= 1
		if i < j:
			comparables[i], comparables[j] = comparables[j], comparables[i]
			i += 1 # essential for duplicate keys
			j -= 1 # essential for duplicate keys

	comparables[lo], comparables[j] = comparables[j], comparables[lo]
	return j


def _qksort(comparables, lo, hi):
	"""Quick sort helper function

	Arguments:
	comparables -- an array of which the elements can be compared
	lo          -- lower bound of indices
	hi          -- higher bound of indices
	"""

	# quick sort too heavy for tiny arrays
	# cutoff to insertion sort
	if hi - lo <= CUTOFF:
		insort(comparables, lo, hi)
		return
	
	# pivot given by "median of three"
	m = _median3(comparables, lo, lo+(hi-lo)//2, hi-1)
	comparables[lo], comparables[m] = comparables[m], comparables[lo]

	j = _partition(comparables, lo, hi)
	_qksort(comparables, lo, j)
	_qksort(comparables, j+1, hi)


def _median3(comparables, lo, mid, hi):
	"""Sort the three elements of an array in ascending order in place and 
	return the middle index

    Arguments:
	comparables -- an array of which the elements can be compared
	lo          -- index 1 (inclusive)
	mid         -- index 2 (inclusive)
	hi          -- index 3 (inclusive)
	"""
	if comparables[lo] > comparables[mid]:
		comparables[lo], comparables[mid] = comparables[mid], comparables[lo]
	if comparables[mid] > comparables[hi]:
		comparables[mid], comparables[hi] = comparables[hi], comparables[mid]
	if comparables[lo] > comparables[mid]:
		comparables[lo], comparables[mid] = comparables[mid], comparables[lo]
	return mid


def _tukey9(comparables, lo, hi):
	"""Return the index pointing to the median of median of nine values

	Arguments:
	comparables -- an array of which the elements can be compared
	lo          -- lower bound of indices (inclusive)
	hi          -- higher bound of indices (exclusive)

	Tukey's ninther is a median of median methods to pick pivot of medium 
	value. In practice, it only involves 9 values, and usually works 
	incredibly well. 
	"""
	pnts = list(range(lo, hi, (hi-lo)//9))
	med1 = _median3(comparables, pnts[0], pnts[1], pnts[2])
	med2 = _median3(comparables, pnts[3], pnts[4], pnts[5])
	med3 = _median3(comparables, pnts[6], pnts[7], pnts[8])
	return _median3(comparables, med1, med2, med3)


def qkselect(comparables, k):
    """Return the kth smallest element in an array, k = 1, 2, ...

    Arguments:
	comparables -- an array of which the elements can be compared
	k           -- an integer indicating k-th order 

    Quick select find the kth smallest element in an array
    """
    assert k >= 1 and k <= len(comparables)
    k -= 1

    shuffle(comparables)
    lo, hi = 0, len(comparables)
    while hi - lo > 1:
        j = _partition(comparables, lo, hi)
        if j < k:
            lo = j + 1
        elif j > k:
            hi = j
        else:
            return comparables[k]
    return comparables[k]


def _qksort3(comparables, lo, hi):
	"""Quick sort helper function using Dijkstra 3-way partition

	Arguments:
	comparables -- an array of which the elements can be compared
	lo          -- lower bound of indices
	hi          -- higher bound of indices
	"""
	if hi - lo <= CUTOFF:
		insort(comparables, lo, hi)
		return
	lt, gt = _partition3(comparables, lo, hi)
	_qksort3(comparables, lo, lt)
	_qksort3(comparables, gt, hi)


def _partition3(comparables, lo, hi):
	"""Partition the array into three parts for which 
	* comparables[lo:lt] < pivot
	* comparables[lt:gt] = pivot
	* comparables[gt:hi] > pivot 
	where pivot is the first elemnt of input

	Arguments:
	comparables -- an array of which the elements can be compared
	lo          -- lower bound of indices
	hi          -- higher bound of indices

	Dijkstra 3-way partition algorithm is used. 

	--------------------------------------
	a b c d e f g g g g g g h i j k l m 
	^           ^           ^           ^
	lo          lt          gt          hi
	--------------------------------------
	"""
	pivot = comparables[lo]
	lt, gt = lo, hi

	i = lo
	while i < gt:
		if comparables[i] < pivot:
			comparables[lt], comparables[i] = comparables[i], comparables[lt]
			lt += 1
			i += 1
		elif comparables[i] > pivot:
			gt -= 1
			comparables[gt], comparables[i] = comparables[i], comparables[gt]
		else: i += 1
	return lt, gt


def hpsort(comparables):
	"""Heap sort an array into ascending order in place

	There are two steps involved in heap sort. In the first step, a max heap 
	is built using bottom-up method. Notice that heap is complete binary tree,
	as a result
	* comparables[0:hi//2] are parent nodes;
	* comparables[hi//2:hi] are leaf nodes. 
	Loop through the parents in "reverse" order (i.e. bottom-up), and 
	repeatedly sink them to restore heap order. 

	In the second step, repeatedly "pop" the largest remaining item and shrink
	the heap size. 

	Caveat: Heap sort has excellent theoretical properties. But it is not 
	optimal in practice. The inner loop takes longer than quick sort, and it 
	makes poor use of cache memory since it references memory all over the 
	place. 
	"""
	#heap construction
	hi = len(comparables)
	for k in reversed(range(hi//2)): 
	#loop through parent nodes of binary heap tree bottom-up
		_sink(comparables, k, hi)

	#sortdown
	while hi - 1 > 0:
		hi -= 1
		comparables[0], comparables[hi] = comparables[hi], comparables[0]
		_sink(comparables, 0, hi)


def _sink(comparables, k, hi):
	"""Sink kth element down to restore heap order in the tree rooted in k up
	to hi (exclusive)

    Arguments:
	comparables -- an array of which the elements can be compared
	k           -- an integer indicating k-th position
	hi          -- higher bound of indices	
	"""
	while 2*k + 1 < hi: 
	# kth node has left child
		j = 2*k + 1
		if j+1 < hi and comparables[j] < comparables[j+1]:
		# kth node has right child & it is larger
			j += 1
		if comparables[k] >= comparables[j]: # already in heap order
			break
		comparables[k], comparables[j] = comparables[j], comparables[k]
		k = j


def bsearch(comparables, key):
	"""Return index when key is found in an ordered array; otherwise return 
	None (binary search)
	
	Parameters:
	comparables -- an ascending ordered array
	key         -- key to be searched 
	"""
	lo, hi = 0, len(comparables)
	while lo < hi:
		mid = lo + (hi - lo)//2
		if comparables[mid] > key: hi = mid
		elif comparables[mid] < key: lo = mid + 1
		else: return mid
	return None


#main guard
if __name__ == '__main__':
	a = list(range(100))
	shuffle(a)
	hpsort(a)
	print(a)