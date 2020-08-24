"""

Bins & Balls
birthday problem 
coupon collector 
loading balancing 

seperate chaining H. P. Luhn, IBM 1953 
linear probing Amdahl-Boehme-Rocherster-Samuel, IBM 1953


Knuth's parking problem
Model. Cars arrive at one-way street with M parking spaces. Each desires a random space i: if space i is taken, try i+1, i+2, ...
Q. What's the mean displacement of a car?
half-full: With M/2 cars, mean displacement is ~ 3/2. 
     full: With M cars, mean displacement is ~sqrt(pi/8 * M)
Proposition. Under uniform hasing assumption, the average # of probes in a linear probing hash table of size M that contains N = aM keys is 
search hit ~ 1/2(1 + 1/(1 - a))
search miss/insert ~ 1/2(1 + 1/(1-a)^2) 

one-way hash function
MD4
MD5
SHA-0
SHA-1
SHA-2
WHIRLPOOL
RIPEMD-160 

two-probe hashing
   double hashing
   cuckoo hashing

"""

class NodeKV:
	"""None terminated linked list of key-value pairs"""
	def __init__(self, key, val):
		self.key = key
		self.val = val
		self.next = None

	def __repr__(self):
		""""""
		return str("{} : {}".format(self.key, self.val))


class HashTable:
	"""Symbol table implemented using a hash table

	N -- number of key-value pairs to be inserted into the symbol table
	M -- size of array (of linked lists) 
	typically, M ~ N/5

	collision resolution:
	* separate chaining 
	* linear probing 
	"""
	def __init__(self):
		"""Initialize an empty symbol table"""
		self.symtab = [] #an array of linked lists
		self.N = 0       #size of elements

	def __len__(self):
		"""Retuen the size of the symbol table"""
		return self.N

	def _resize(self, size):
		pass 

	def get(self, key):
		"""Get value corresponding to key in the symbol table
		
		The symbol table is implemented using a hash table where overlapping
		keys are separated using "separated chaining".
		"""
		index = hash(key)
		node = self.st[index]
		while node is not None:
			if  key == node.key:
				return node.val
			else:
				node = node.next
		return None 

	def put(self, key, val):
		""""""
		index = hash(key)
		node = self.st[index]
		while node is not None:
			if key == node.key:
				node.val = val
				break
			else:
				node = node.next
		st[index] = Node(key, val, st[index])


def hash_(n):
	"""Return an integer between 0 (inclusive) and n (exclusive)"""
	pass 

class HTable:
	def __init__(self):
		"""Initialize an empty hash table for which collision is resolved
		using "linear probing"

		M should be kept smaller than N/2 to (statistically) guarantee hash performance. 
		"""
		self.keys = [] #array of keys
		self.vals = [] #array of values
		self.N = 0     #size of key-value pairs 
		self.M = 0     #size of array (capacity)

	def __len__(self):
		"""pass"""
		return self.N

	def put(self, key, val):
		""""""
		index = hash(key)
		while self.keys[index] is not None:
			if key == self.keys[index]:
				break
			index = (index + 1) % self.M
		keys[index] = key 
		vals[index] = val

	def get(self, key):
		""""""
		index = hash(key)
		while self.keys[index] is not None:
			if key == self.keys[index]:
				return self.vals[index]
			index = (index+1) % M
		return None
