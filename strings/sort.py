"""STRING SORT

STRING -- sequence of characters 

C : 7-bit ASCII (letters|numbers|punctuations)
unicode : 16-bit unsigned integer
unicode 3.0 : 21-bit unsigned integer 
Java : immutable sequence of characters
Python : immutable sequence of characters

sublinear time

"""

"""CONSTANTS

name           |  R()  | lgR() | characters
-----------------------------------------------------------
BINARY         |     2 |   1   | 01
OCTAL          |     8 |   3   | 01234567
DECIMAL        |    10 |   4   | 0123456789
HEXADECIMAL    |    16 |   4   | 0123456789ABCDEF
DNA            |     4 |   2   | ACTG
LOWERCASE      |    26 |   5   | abedefghijklmnopqrstuvwxyz
UPPERCASE      |    26 |   5   | ABCDEFGHIJKLMNOPQRSTUVWXYZ
PROTEIN        |    20 |   5   | ACDEFGHIKLMNPQRSTVWY
BASE64         |    64 |   6   | ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/
ASCII          |   128 |   7   | ASCII characters
EXTENDED_ASCII |   256 |   8   | extended ASCII characters
UNICODE16      | 65536 |  16   | Unicode characters
-----------------------------------------------------------
"""

"""KEY-INDEXED COUNTING
1-pass count frequency
2-pass compute cumulates
3-pass move items 
4-pass copy back 
Time ~ 11N + 4R; Space ~ N + R
stable 
"""

LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

RADIX = 256

def kicount(keys):
	"""Sort keys using key-indexed counting. Make sure keys are mapped to 
	0, 1, ... N-1 where N is number of distinct keys. 
	
	Arguments:
	- keys: a collections of keys (represented by 0, 1, ... N-1)
	"""
	n = len(keys)
	count = [0] * (RADIX + 1)

	#pass 1 -- counting 
	for key in keys: count[key+1] += 1
	#pass 2 -- cumulative counting 
	for i in range(RADIX): count[i+1] += count[i]
	#pass 3 -- sorting 
	aux = keys[:]
	for key in keys:
		aux[count[key]] = key
		count[key] += 1
	#pass 4 -- copying 
	for i in range(n): keys[i] = aux[i]


"""LSD string (radix) sort
LSD -- least-significant-digit-first string sort 
- consider characters from right to left;
- stably sort using dth character as the key (using key-indexed couting).
"""
class LSD:
	"""Least-significant-digit-first string sorting"""
	def sort(self, a):
		"""
		Arguments:
		a - an array of fixed-length strings
		W - length (width) of a string
		"""
		assert(len(set([len(s) for s in a])) == 1)

		N, W = len(a), len(a[0])
		aux = a[:]

		for d in reversed(range(W)):
		#key-indexed counting for each digit from right to left
			count = [0]*(R+1)
			#key-indexed counting
			for i in range(N): count[ord(a[i][d]) + 1] += 1
			for i in range(RADIX): count[i+1] += count[i]
			for i in range(N): 
				aux[count[ord(a[i][d])]] = a[i]
				count[ord(a[i][d])] += 1
			for i in range(N): a[i] = aux[i]


"""MSD string (radix) sort
MSD -- most-significant-digit-first string sort

"""

#treat strings as if they had an extra char at end (smaller than any char)
def ordinal(string, d):
	"""Return the ordinal of the character at dth position. 
	Specifically, the ordinal of end-of-string is defined to be -1.
	"""
	if d < len(string): 
		return ord(string[d])
	elif d == len(string): 
		return -1
	else: 
		raise IndexError 


CUTOFF = 7

def msd(a):
	"""Most-Significant Digit string sort the list of strings in ascending
	order"""
	aux = a[:] #can recycle aux[] array
	_sort(a, aux, 0, len(a), 0)

def _sort(a, aux, lo, hi, d):
	"""Sort the dth digit of strings from lo to (hi-1) in ascending order

	Arguments: 
	a   -- list of strings to be sorted, a[i][d] is dth digit of ith string
	aux -- auxiliary array (recyclable)
	lo  -- lower bound of array index
	hi  -- higher bound of array index
	d   -- dth digit

	Caveat: 
	RADIX+1 distinct characters, one extra for end-of-string character;
	Cutoff to insertion sort for small sub-lists;

	count 
		 0
	\0   5
	a    7
	b    10
	"""
	#recursion return condition
	if lo >= hi-1: return 

	#cutoff to insertion sort 
	if lo >= hi - CUTOFF: 
		for i in range(lo, hi):
			for j in range(i, lo, -1):
				if a[j-1][d:] < a[j][d:]: break
				a[j-1], a[j] = a[j], a[j-1]

	#key-indexed counting (extra end-of-string character)
	count = [0] * (RADIX + 2) #cannot recycle count[] array
	for i in range(lo, hi):  #pass 1 -- counting 
		count[ordinal(a[i], d) + 2] += 1

	for i in range(RADIX+1): #pass 2 -- cumulative sum
		count[i+1] += count[i]

	for i in range(lo, hi):  #pass 3 -- sorting 
		aux[count[ordinal(a[i], d) + 1]] = a[i]
		count[ordinal(a[i], d) + 1] += 1

	for i in range(lo, hi):  #pass 4 -- copying 
		a[i] = aux[i-lo]

	#sort R subarrays recursively	
	for i in range(1, RADIX+1): 
		_sort(a, aux, lo+count[i], lo+count[i+1], d+1)


"""Standard quicksort
* uses ~ 2NlgN string compares on average
* costly for keys with long common prefixes (common case)

3-way string (radix) quicksort
* uses ~ 2NlgN character compares on average 
* avoids re-comparing long common prefixes

Bentley & Sedgewick (1999) Fast algorithms for sorting and searching strings
"""
def qksort(a):
	"""3-way string quicksort"""
	_qksort(a, 0, len(a), 0)

def _qksort(a, lo, hi, d):
	"""Quick sort the dth digit of subarray from lo (inclusive) to hi 
	(exclusive) in ascending order. 

	Compared to MSD string sort, 3-way sting quicksort 
	* has a short inner loop
	* is cache-friendly
	* is in-place

	Bottom line -- 3-way string quicksort is method of choice for sorting strings
	"""
	if lo >= hi-1: return 
	#3-way partitioning (using dth character)
	# a b c d e e e e f g h i
	# ^       ^       ^       ^
	#lo      lt      gt      hi
	lt, gt = lo, hi
	pivot = ordinal(a[lo], d) #to handle variable-length strings
	i = lo + 1
	while i < gt:
		t = ordinal(a[i], d) #to handle variable-length strings
		if t < pivot: 
			a[lt], a[i] = a[i], a[lt] 
			lt += 1
			i += 1
		elif t > pivot:
			gt -= 1
			a[i], a[gt] = a[gt], a[i]
		else:
			i += 1
	#sort 3 subarrays recursively 
	_qksort(a, lo, lt, d)
	if pivot >= 0: _qksort(a, lt, gt, d+1)
	_qksort(a, gt, hi, d) 


"""Keyword-in-context search
given a text of N characters, preprocess it to enable fast substring search

suffix sort
input string
i t w a s b e s t i t w a s w

form suffixes                    sort suffixes to bring repeated substrings together
i t w a s b e s t i t w a s w    a s b e s t
t w a s b e s t i t w a s w      a s w
w a s b e s t i t w a s w        b e s t i t w a s w 
a s b e s t i t w a s w          e s t i t w a s w 
s b e s t i t w a s w            i t w a s b e s t i t w a s w 
b e s t i t w a s w              i t w a s w 
e s t i t w a s w                s b e s t i t w a s w 
s t i t w a s w                  s t i t w a s w 
t i t w a s w                    s w 
i t w a s w                      t i t w a s w 
t w a s w                        t w a s b e s t i t w a s w 
w a s w                          t w a s w 
a s w                            w 
s w                              w a s b e s t i t w a s w 
w                                w a s w 
"""

#longest repeated substring 
def lrs(string):
	"""Return longest repeated substring of a given string"""
	n = len(string)
	#create suffixes (time & space)
	suffixes = [string[i:] for i in range(n)]
	#sort suffixes
	qksort(suffixes)
	lrs = ""
	#find lcp between adjacent suffixes in sorted order
	for i in range(n-1):
		len_ = lcp(suffixes[i], suffixes[i+1])
		if len_ > len(lrs):
			lrs = suffixes[i][:len_]
	return lrs 


def lcp(s1, s2):
	"""Return longest common prefix of two strings"""
	for i, (c1, c2) in enumerate(zip(s1, s2)):
		if c1 != c2: return i
	return i

"""Manber-Myers MSD algorithm
phase 0: sort on first character using key-indexed counting sort;
phase i: given array of suffixes sorted on first 2**(i-1) characters, create
array of suffixes sorted on first 2**i characters.
"""

"""Tries (reTRIEval, but pronounced "try")
- store characrers in nodes (not key)
- each node has R children, one for each possible character
- store values in nodes correpondding to last character in keys

string symbol table -- symbol table specialized to string keys

implementation | search hit | search miss | insert  | space 
 red-black BST | L + clg2N  | clg2N       | clg2N   | 4N
       hashing | L          | L           | L       | 4-16N
    R-way trie | L          | logR(N)     | L       | (R+1)N
    TST        | L + lnN    | lnN         | L + lnN | 4N

bottom line: fast search hit & faster search miss, but wastes spaces
"""

class TrieNode:
	"""Node for trie"""
	def __init__(self, val=None, next=[None]*RADIX):
		self.val = val
		self.next = next 

class TrieST:
	"""Trie symbol table"""
	def __init__(self, arg):
		"""Initialize an empty R-way trie"""
		self.root = None

	def put(self, key, val):
		"""Put key-value pair into the trie"""
		self.root = self._put(self.root, key, val, 0)

	def _put(self, node, key, val, d):
		"""Put dth digit of key on the trie"""
		if node == None: node = TrieNode()
		if d == len(key): 
			node.val = val
			return node 
		c = key[d]
		node.next[ord(c)] = self._put(node.next[ord(c)], key, val, d+1)
		return node 

	def __contains__(self, key):
		"""Return True if key is in the trie"""
		return self.get(key) is not None

	def get(self, key):
		"""Return value paired with key"""
		node = self._get(self.root, key, 0)
		if node is None: return 
		return node.val

	def _get(self, node, key, d):
		""""""
		if node is None: return #not found 
		if d == len(key): return node #at last char, return node
		c = key[d]
		return self._get(node.next[ord(c)], key, d+1) #move down the tree

	def delete(self, key):
		"""Delete key and corresponding value"""
		pass

	def keys(self):
		"""Return all keys"""
		#inorder traversal of trie
		queue = Queue()
		self._collect(self.root, "", queue)
		return queue 

	def _collect(self, node, prefix, queue):
		if node is None: return None
		if node.val is not None: queue.enqueue(prefix)
		for char in range(RADIX):
			self._collect(node.next, prefix + char, queue)

	def keys_prefix(self, prefix):
		"""Return keys with given prefix"""
		queue = Queue()
		#sub-trie for string beginning with given prefix
		node = self._get(self.root, prefix, 0)
		self._collect(node, prefix, queue)
		return queue

	def keys_match(self, pattern):
		"""Return keys matching a pattern (where . is a wildcard)"""
		pass

	def longest_prefix(self, query):
		"""Return longest key that is a prefix of query string"""
		length = self._search(self.root, query, 0, 0)
		return query[:length]

	def _search(self, node, query, d, length):
		""" """
		if node is None: return length
		if node.val is not None: length = d 
		if d == len(query): return length 
		char = query[d]
		return self._search(node.next[char], query, d+1, length)

	def floor(self, key):
		pass

	def rank(self, key):
		pass


"""Ternary serch tries
* store characters and values in nodes (not keys)
* each node has 3 children: smaller (left), equal (middle) and larger (right)

key is sequence of characters from root to value using middle link
value is in node corresponding to last character

TST vs hashing
hashing
* need to examine entire key;
* search hits and misses cost about the same
* performance relies on hash function
* does not support ordered symbol table operations

TSTs
* works only for strings (or digital keys)
* only examines just enough key characters
* search miss may involve only a few characters
* supports ordered symbol table operations 

bottomline -- TSTs are 
* faster than hashing (especially for search misses)
* more flexible than red-black BSTs
"""

class TstNode:
	"""Ternary search trie node"""
	def __init__(self, val, char, left=None, mid=None, right=None):
		self.val = val
		self.char = char
		self.left = left
		self.mid = mid
		self.right = right
		

class TST:
	"""Ternary search trie"""
	def __init__(self):
		"""Initialize an empty trie"""
		self.root = None #empty trie

	def put(self, key, val):
		"""Put key-value pair on the trie"""
		self.root = self._put(self.root, key, val, 0)

	def _put(self, node, key, val, d):
		"""Put key[d:]-value pair on the sub-trie rooted at node"""
		char = key[d]
		if node is None: node = TstNode(None, char)
		if char < node.char: 
			node.left = self._put(node.left, key, val, d)
		elif char > node.char: 
			node.right = self._put(node.right, key, val, d)
		elif d + 1 < len(key): #not end-of-string yet
			node.mid = self._put(node.mid, key, val, d+1)
		else: #end-of-string
			node.val = val 
		return node 

	def __contains__(self, key):
		"""Return True if key is in trie"""
		return self.get(key) is not None

	def get(self, key):
		"""Get the value associated with key"""
		node = self._get(self.root, key, 0)
		if node is None: return None
		return node.val 

	def _get(self, node, key, d):
		"""Get the value associated with key[d:] from sub-trie 
		rooted at node"""
		if node is None: return None
		char = key[d]
		if char < node.char:
			return self._get(node.left, key, d)
		elif char > node.char:
			return self._get(node.right, key, d)
		elif d + 1 < len(key):
			return self._get(node.mid, key, d+1)
		else:
			return node 


"""Patricia trie (Practical Algorithm to Retrieve Information Coded in Alphanumeric)
* remove one-way branching
* each node represents a sequence of characters
"""

"""
suffix table
suffix array
suffix tree  
"""

#test case
if __name__ == "__main__":
	from sort import shuffle
	a = ["are", "by", "sea", "seashells", "seashells", "sells", "sells", "she", "she", "shells", "shore", "surely", "the", "the"]
	shuffle(a)
	print(a)
	qksort(a)
	print(a)