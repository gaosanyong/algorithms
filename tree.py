"""TREE-BASED ALGORITHMS"""

"""PRIORITY QUEUE (HEAP)
implementation  | insert | del max | max   |
--------------------------------------------
unordered array | 1      | N       | N     |
      Fibonacci | 1      | logN    | 1     |
     d-ary heap | logdN  | dlogdN  | 1     |
    binary heap | logN   | logN    | l     |
  ordered array | N      | 1       | 1     |
--------------------------------------------

In this library, the priority queue is implemented using a binary heap, which 
is an (implicit) array representation of a heap-ordered complete binary tree.

				  +
				/   \
			   +     +
			  / \   / \
			 +   + +   +
      
A complete tree is a perfectly balanced tree except for the bottom level. Thus, 
* to move from child to parent, k -> (k-1)//2
* to move from parent to child, k -> 2*k+1, 2*k+2

A max heap-order is an order for which parent's key is no smaller than 
children's keys; while in a min heap-order parent's key is no larger than 
children's keys.
"""

class Fenwick: 
    """Fenwick tree (Peter Fenwick 1994) aka binary indexed tree (BIT) is a 
    tree data structure implemented via array to efficiently compute prefix 
    sums."""

    def __init__(self, n: int):
        """Initialize a Fenwick tree with n values."""
        self.nums = [0]*(n+1)

    def query(self, k: int) -> int: 
        """Return the prefix sum aka sum(nums[:k+1])."""
        k += 1
        ans = 0
        while k:
            ans += self.nums[k]
            k -= k & -k # unset last set bit 
        return ans

    def add(self, k: int, x: int) -> None: 
        """Add the kth element with value x to Fenwick tree."""
        k += 1
        while k < len(self.nums): 
            self.nums[k] += x
            k += k & -k 

			
from containers import Queue, MAXSIZE

class PQueue:
	"""A priority queue object is a queue where each element has a "priority"
	and thus elements with high priority are before elements with low priority. 
	"""
	def __bool__(self):
		"""Return True if priority queue is non-empty"""
		return bool(self._N)

	def __init__(self, queue=[]):
		"""Initialize a heap implemented (empty) priority queue"""
		self._pq = queue     #underlying array to host priority queue
		self._N = len(queue) #queue size (not array size)

	def __iter__(self):
		"""Return an iterator to loop through the priority queue"""
		self._temp = self._pq.copy()
		return self
		
	def __len__(self):
		"""Return the size of the priority queue"""
		return self._N

	def __next__(self):
		"""Return the next item in the priority queue"""
		if len(self) == 0:
			self._pq = self._temp
			del self._temp
			raise StopIteration
		return self.delete()		

	def __repr__(self):
		"""Print priority queue as the underlying array"""
		return str(self._pq[:len(self)])

	def _isordered(self, p, c):
		"""Return True if 
		1) parent (p) and child (c) are in heap order, or
		2) left child and right child are in appropriate order
		
		True table
		--------------------------------
		max heap | p >= c | left < right
		min heap | p <= c | left > right
		--------------------------------
		
		This is the only method where max queue differs from min queue.
		"""
		pass 

	def _resize(self, size):
		"""Resize the underlying array to given size"""
		if size > MAXSIZE:
			raise Exception("Priority queue overflow")

		assert size >= len(self)
		self._pq = self._pq[:len(self)] + [None]*(size-len(self))

	def _sink(self, k):
		"""Sink down element at k until heap order is restored

		Argument(s): 
		k           -- the index of the element to be sinked
		In force is the "power struggle", i.e. better subordinate is promoted 
		"""
		while 2*k + 1 < len(self):
		#check if node has left child
			c = 2*k + 1 #left child
			if c + 1 < len(self) and not self._isordered(c, c+1):
			#check if node has right child & right child is larger
				c += 1 #right child
			if self._isordered(k, c): 
				break
			self._pq[k], self._pq[c] = self._pq[c], self._pq[k]
			k = c

	def _swim(self, k):
		"""Swim up element at k until heap order is restored
		Argument(s):
		k           -- the index of the element to be promoted
		In force is the "Peter principle", i.e. node is promoted to level of 
		incompetence
		"""
		while k > 0:
		#check non-root
			p = (k-1)//2 #parent of k
			if self._isordered(p, k): #self._pq[p] >= self._pq[k]: #heap order
				break
			self._pq[p], self._pq[k] = self._pq[k], self._pq[p]
			k = p

	def delete(self):
		"""Delete the maximum element from the priority queue

		Pop the element at the front of the priority queue, move the element
		at the rear to the front, and sink it down until heap order is 
		restored. 
		"""
		if len(self) == 0:
			raise Exception("Priority queue underflow")

		self._N -= 1

		item = self._pq[0]
		self._pq[0], self._pq[self._N] = self._pq[self._N], self._pq[0]
		self._pq[self._N] = None # prevent loitering 
		self._sink(0)

		if len(self) == len(self._pq)//4: #thrashing 
			self._resize(len(self._pq)//2)

		return item 

	def insert(self, item):
		"""Insert a new item to the priority queue

		Insert the new item at the rear of the priority queue, and swim it up
		until heap order is restored. 

		Argument(s):
		item        -- item to be inserted 
		"""
		if len(self) == len(self._pq): 
		#check if queue has reached capacity
			self._resize(2*len(self) + (len(self)==0)) # repeated doubling 

		self._pq[self._N] = item
		self._swim(self._N)
		self._N += 1


class MinQueue(PQueue):
	"""A minimum queue object is a queue where smaller element has a higher 
	priority.
	"""
	def _isordered(self, p, c):
		"""Return True if in minimum heap order (i.e. parent <= child) 
		"""
		return self._pq[p] <= self._pq[c]


class MaxQueue(PQueue):
	"""A maximum queue object is a queue where larger element has a higher
	priority.
	"""
	def __isordered(self, p, c):
		"""Return True if in maximum heap order (i.e. parent >= child).
		"""
		return self._pq[p] >= self.pq[c]


def heapify(array):
	"""In-place heapify array into a min heap"""
	for i in range(len(array)):
		#swim up the ith element
		while i: 
			j = (i-1)//2
			if array[j] <= array[i]: break
			array[i], array[j] = array[j], array[i]
			i = j 

"""A symbol table is an interface which return value for a query key

 implementation | ins/del | search  | min/max | floor/ceiling | rank    | select  | 
-----------------------------------------------------------------------------------
    linked list | O(N)    | O(N)    | 
  ordered array | O(logN) | O(logN) | 
unordered array | O(N)    | O(N)    | 
bin search tree | O(logN) | O(logN) | O(logN) | O(logN)       | O(logN) | O(logN) |
     hash table | 
----------------------------------------------------------
A symbol table is implemented 

Equality test (equivalence relation)
(1) Reflexive: x == x
(2) Symmetric: x == y iff y == x
(3) Transitive: if x == y and y == z, then x == z
(4) Not None: nothing equals to None

Binary search tree (BST) is a binary tree in "symmetric" order, where each 
node has a key that is larger than all keys in its left subtree, and smaller 
than all keys in its right subtree (duplicate not allowed).

|----------------------------------------------------|
| keys in left subtree < key < keys in right subtree |
|----------------------------------------------------|

Compare to "heap" order where key >= keys in all subtrees

BST has a 1-to-1 correspondence to quicksort partitioning if no duplicate keys.
However, we don't have the luxury to shuffle the input stream which is controled by client. 

-------------------------------------------------------------------
 depth-first traversal |   inorder* | left -> root -> right | stack 
                       |  preorder  | root -> left -> right | stack
                       | postorder  | left -> right -> root | stack 
breath-first traversal |                                    | queue 
-------------------------------------------------------------------
"""

RED = True
BLACK = False

class TreeNode:
	"""Node in a binary search tree"""
	def __init__(self, key, val, color=RED):
		"""Initialize an node on BST with key-val pair

		Arguments:
		key   -- key
		val   -- value 
		left  -- link to left child
		right -- link to right child
		count -- size of subtree rooted at this node
		color -- RED/BLACK in left-leaning red-black (LLRB) BST 
		"""
		self.key = key
		self.val = val
		self.left = None   #link to left child
		self.right = None  #link to right child
		self.count = 1     #size of subtree rooted at this node
		self.color = color #color in left-leaning red-black (LLRB)

	def __len__(self):
		"""Return the size of the (sub)tree rooted at this node"""
		return self.count

	def __repr__(self):
		"""Return the string representation"""
		return str(self.val)

	def isred(self):
		"""Return True if node is RED"""
		if self.node == None:
			return False
		return self.color == RED


class BSTree:
	"""Symbol Table API"""
	def __init__(self):
		"""Initialize an empty symbol table (BST implementation)"""
		self.root = None

	def __iter__(self):
		"""Inorder traversal (depth-first traversal)"""
		self.queue = Queue()
		self._inorder(self.root, self.queue)
		return self

	def __len__(self):
		""""""
		if self.root is None:
			return 0
		else:
			return self._size(self.root) 

	def __next__(self):
		"""Return next element when looping through BST"""
		if len(self.queue) == 0:
			del self.queue
			raise StopIteration
		return self.queue.dequeue()

	def __repr__(self):
		"""How to visualize a BST???"""
		pass

	def _inorder(self, node, queue):
		"""Depth-first inorder traverse the tree"""
		if node is None:
			return
		self._inorder(node.left, queue)
		queue.enqueue(node.key)
		self._inorder(node.right, queue)

	def _size(self, node):
		"""Return the size of subtree rooted at node"""
		if node is None:
			return 0
		else:
			return node.count 

	def contains(self, key):
		"""Return True if key exists"""
		node = self.get(key)
		if node is None:
			return False
		else:
			return True

	def put(self, key, val):
		"""Put a key-value pair into the symbol table"""
		self.root = self._put(self.root, key, val)

	def _put(self, node, key, val):
		"""Depending on how the keys coming in, the BST will look different"""
		if node is None:
			return TreeNode(key, val)
		if key < node.key:
			node.left = self._put(node.left, key, val)
		elif key > node.key:
			node.right = self._put(node.right, key, val)
		else:
			node.val = val
		node.count = 1 + self._size(node.left) + self._size(node.right)
		return node

	def get(self, key):
		"""Return value paird with key"""
		node = self.root
		while node is not None:
			if key < node.key:
				node = node.left
			elif key > node.key:
				node = node.right
			else:
				return node.val 
		return None

	def delete(self, key):
		"""Delete key-value pair from the table

		Hibbard deletion
		*  no children, 
		* one children, 
		* two children, 
		"""
		self.root = self._delete(self.root, key)

	def _delete(self, node, key):
		"""Hibbard deletion workhorse function"""
		#fixme: need delete for left-leaning red-black tree
		if node is None:
		#no children
			return None

		if key < node.key:
			node.left = self._delete(node.left, key)
		elif key > node.key:
			node.right = self._delete(node.right, key)
		else:
			#one children
			if node.right is None: return node.left
			if node.left is None: return node.right

			#two children
			temp = node 
			node = self.min(node.right)
			node.right = self.delmin(temp.right)
			node.left = temp.left
		node.count = self._size(node.left) + self._size(node.right) + 1
		return node 

	def isempty(self):
		"""Return True if table is empty"""
		return len(self) == 0

	def min(self):
		"""Return the node with minimum key"""
		node = self.root
		while node.left is not None:
			node = node.left
		return node.key

	def max(self):
		"""Return the node with maximum key"""
		node = self.root
		while node.right is not None:
			node = node.right
		return node.key

	def floor(self, key):
		"""Return the largest key on BST that is less than or equal to (<=) 
		the given key
		"""
		node = self._floor(self.root, key)
		if node is None:
			return None
		return node.key

	def _floor(self, node, key):
		"""floor workhorse function"""
		if node is None:
			return None
		if key == node.key:
			return node
		if key < node.key:
			return self._floor(node.left, key)
		temp = self._floor(node.right, key)
		if temp is not None:
			return temp
		else:
			return node

	def ceiling(self, k):
		"""Return the smallest key on BST that is larger than or equal to (>=)
		the given key
		"""
		node = self._ceiling(self.root, key)
		if node is None:
			return None
		return node.key

	def _ceiling(self, node, key):
		"""ceiling workhorse function"""
		if node is None:
			return None
		if key == node.key:
			return node
		if key > node.key:
			return self._ceiling(node.right, key)
		temp = self._ceiling(node.left, key)
		if temp is not None:
			return temp
		else:
			return node 

	def rank(self, key):
		"""Return the number of keys less than (<) the given key"""
		return self._rank(self.root, key)

	def _rank(self, node, key):
		""""""
		if node is None:
			return 0
		if key < node.key:
			return self._rank(node.left, key)
		elif key > node.key:
			return 1 + self._size(node.left) + self._rank(node.right, key)
		else:
			return self._size(node.left)	

	def delmin(self):
		"""Delete the node with minimum key"""
		self.root = self._delmin(self.root)

	def _delmin(self, node):
		"""delmin workhorse function"""
		if node.left is None:
			return node.right
		node.left = self._delmin(node.left)
		node.count = 1 + self._size(node.left) + self._size(self.right)
		return node

	def delmax(self):
		"""Delete the node with maximum key"""
		self.root = self._delmax(self.root)

	def _delmax(self, node):
		"""delmax workhorse function"""
		if node.right is None:
			return node.left
		node.right = self._delmax(node.right)
		node.count = 1 + self._size(node.left) + self._size(self.right)
		return node


def fcounter(istream):
	"""Frequency counter client
	Count frequency of words 
	"""
	stable = ST
	for word in istream:
		if word not in stable:
			st.put(word, 1)
		else:
			st.put(word, st.get(word) + 1)
	max_ = ""
	st.put(max_, 0)
	for word in st.keys():
		if st.get(word) > st.get(max_):
			max_ = word
	return max_, st.get(max_)


class SegTree: 
    """A segment tree, aka a statistic tree, is a tree data structure used for 
    storing information about intervals. It allows querying which of the stored 
    segments contain a given point."""

    def __init__(self, arr: List[int]): 
        """Build the setmentation tree."""
        self.n = len(arr)
        self.tree = [0]*(4*self.n)
        self._build(arr, 0, 0, self.n)

    def _build(self, arr: List[int], k: int, lo: int, hi: int) -> None: 
        """Build segment tree from array."""
        if lo+1 == hi: 
            self.tree[k] = arr[lo]
            return 
        mid = lo + hi >> 1
        self._build(arr, 2*k+1, lo, mid)
        self._build(arr, 2*k+2, mid, hi)
        self.tree[k] = min(self.tree[2*k+1], self.tree[2*k+2])

    def update(self, idx: int, val: int, k: int = 0, lo: int = 0, hi: int = 0) -> None:
        """Update segment tree when an array value is changed."""
        if not hi: hi = self.n
        if lo+1 == hi: 
            self.tree[k] = val 
            return 
        mid = lo + hi >> 1
        if idx < mid: 
            self.update(idx, val, 2*k+1, lo, mid) 
        else: 
            self.update(idx, val, 2*k+2, mid, hi)
        self.tree[k] = min(self.tree[2*k+1], self.tree[2*k+2])

    def query(self, qlo: int, qhi: int, k: int = 0, lo: int = 0, hi: int = 0) -> int: 
        """Query value from qlo (inclusive) and qhi (exclusive)."""
        if not hi: hi = self.n
        if qlo <= lo and hi <= qhi: return self.tree[k] # total overlap 
        if qhi <= lo or  hi <= qlo: return inf # no overlap 
        mid = lo + hi >> 1 # partial overlap 
        return min(self.query(qlo, qhi, 2*k+1, lo, mid), self.query(qlo, qhi, 2*k+2, mid, hi))


class WaveletTree:
	pass 
	


if __name__ == "__main__":
	import string
	from sort import shuffle
	from random import randint

	istream = string.ascii_lowercase
	shuffle(list(istream))