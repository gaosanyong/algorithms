"""ARRAY-BASED CONTAINERS

An array is an index-based collection of elements. An array is stored 
contiguously in memory. As a result, arrays have better "cache" locality 
compared to linked lists. 

For some linked list-based counterparts, please see "linkedlist" module. 

class | insertion | iterate | peek | removal
--------------------------------------------
Bag   | O(1)      | O(N)    | O(1) | N/A
Stack | O(1)      | O(N)    | O(1) | O(1)
Queue | O(1)      | O(N)    | O(1) | O(1)
--------------------------------------------
"""

MAXSIZE = float("inf") #max size (overflow)

class Bag:
	"""A bag object is an unordered collection of elements. Bag operations
	include:
	1) adding an element to the bag (removing not allowed),
	2) testing if the bag is empty, 
	3) iterating through the bag. 
	"""

	def __bool__(self):
		"""Return True for non-empty bag"""
		return self._N != 0

	def __init__(self, array=[]):
		"""Initialize an array implementation of (empty) bag"""
		self._array = array  #underlying container
		self._N = len(array) #bag size 

	def __iter__(self):
		"""Return an iterator to loop through the bag

		Caveat: cannot return underlying array as it contains elements not 
		belonging to bag"""
		self._i = 0
		return self

	def __len__(self):
		"""Return the size of the bag"""
		return self._N

	def __next__(self):
		"""Return the next element in the bag"""
		if self._i == self._N:
			del self._i
			raise StopIteration
		item = self._array[self._i]
		self._i += 1
		return item 

	def __repr__(self):
		"""Print elements in the bag"""
		return str(self._array[:self._N])

	def _resize(self, size):
		"""Resize the underlying array upon request"""
		if size > MAXSIZE:
			raise Exception("Bag overflow")

		assert size >= len(self)
		assert size >= len(self._array)
		#array should not shrink in size
		self._array += (size - len(self._array)) * [None]

	def add(self, item):
		"""Add an element to the bag"""
		if self._N == len(self._array):
			self._resize(2*self._N + (self._N == 0)) #repeated doubling
		self._array[self._N] = item 
		self._N += 1


class Stack:
	"""A stack object is an ordered collection of elements, which can be added
	or removed at "top". Stack operations include:
	1) pushing an item onto the stack, 
	2) poping an item off the stack, 
	3) checking if the stack is empty, 
	4) peeking the element on the top of the stack,
	5) iterating through the stack. 

			-------------
	        | top >     |
	        |       --  |
	        |       --  |
	        |       --  |
	        |       --  |
	        |       --  |
            -------------

	Trying to pop an element off an empty stack is called "underflow".
	Whilst a stack is conceptually unbounded, it is desirable to fix the 
	maximum number of elements on a stack - thus excessive pushs will cause
	a stack to "overflow".

	Stacks are also known as LIFOs (last in, first out).
	"""
	def __bool__(self):
		"""Return True for non-empty bag"""
		return self._top != 0

	def __init__(self, array=[]):
		"""Initialize an array implementation of (empty) stack"""
		self._array = array
		self._top = len(array)    #top of the stack

	def __iter__(self):
		"""Return an iterator to loop through stack"""
		self._i = 0
		return self

	def __len__(self):
		"""Return the stack size ~O(1)"""
		return self._top

	def __next__(self):
		"""Return next item on the stack"""
		if self._i == len(self):
			raise StopIteration
		item = self._array[self._i]
		self._i += 1
		return item 

	def __repr__(self):
		"""Return string representation of stack"""
		return str(self._array[:self._top])

	def _resize(self, size):
		"""Resize underlying array to given size

		If new size is larger than existing capacity, 
		extend array with None's; if new size is smaller 
		than existing capacity, cut array.
		"""
		if size > MAXSIZE:
			raise Exception("Stack overflow")

		assert size >= len(self)
		self._array = self._array[:len(self)] + [None]*(size-len(self))

	def peek(self):
		"""Peek top item on stack"""
		if len(self) == 0:
			return None
		else:
			return self._array[self._top-1]

	def pop(self):
		"""Pop item out of the stack ~ amortized O(1)
	
		Once the stack is 1/4 full, "thrashing" is 
		to halve the capacity of the stack  
		"""
		if len(self) == 0:
			raise Exception("Stack underflow")
		self._top -= 1
		item = self._array[self._top]
		self._array[self._top] = None  #prevent loitering

		if len(self) == len(self._array) // 4:
			self._resize(len(self._array) // 2) # thrashing 

		return item  

	def push(self, item):
		"""Push item onto the stack ~ amortized O(1)

		Once the stack is full, "repeated doubling"
		is used to double the capacity of the stack
		"""
		if len(self) == len(self._array):
			self._resize(len(self) * 2 + (len(self) == 0)) # repeated doubling

		self._array[self._top] = item
		self._top += 1


class Queue:
	"""A queue object is an ordered collection of elements, which can be added
	at rear, and removed at front. Queue operations include:
	1) enqueuing an item onto the rear of the queue, 
	2) dequeuing an item from the front of the queue, 
	3) checking if the queue is empty or full, 
	4) peeking the element at the front of the queue.

	---------------------------------------------
    |   < < < < < < < < < < < < < < < < < <     |
	|   ^                                   ^   |
	| front                                rear |
	---------------------------------------------

	Trying to dequeue an item off an empty queue is called "underflow".
	Whilst a queue is conceptually unbounded, it is desirable to fix the 
	maximum number of elements on a queue - thus excessive enqueues will cause
	the queue to "overflow".
	
	Queues are also known as FIFOs (first in, first out).
	"""

	def __bool__(self):
		"""Return True for non-empty bag"""
		return self._front != self._rear

	def __init__(self, array=[]):
		"""Initialize an array implementation of (empty) queue"""
		self._array = array
		self._front = 0          #front of the queue
		self._rear  = len(array) #rear of the queue 

	def __iter__(self):
		"""Return an iterator to loop through the queue"""
		self._i = self._front
		return self

	def __len__(self):
		"""Return the queue size ~ O(1)"""
		return self._rear - self._front

	def __next__(self):
		"""Return the next item in the queue"""
		if self._i == self._rear:
			del self._i
			raise StopIteration

		item = self._array[self._i]
		self._i += 1
		return item 

	def __repr__(self):
		"""Return string representation of queue"""
		return str(self._array[self._front:self._rear])

	def _resize(self, size):
		"""Resize underlying array to give size and reset front & rear pointers"""
		if size > MAXSIZE:
			raise Exception("Queue overflow")

		assert size >= len(self)
		self._array = self._array[self._front:self._rear] + [None]*(size-len(self))
		self._front, self._rear = 0, len(self)

	def dequeue(self):
		"""Dequeue an item from the front of the queue ~ amortized O(1)"""
		item = self._array[self._front]
		self._array[self._front] = None  #prevent loitering
		self._front += 1
		if len(self) == len(self._array) // 4: #thrashing
			self._resize(len(self._array) // 2)
		return item 

	def enqueue(self, item):
		"""Enqueue an item onto the rear of the queue ~ amortized O(1)"""
		if self._rear == len(self._array):
			self._resize(len(self) * 2 + (len(self) == 0)) 

		self._array[self._rear] = item
		self._rear += 1

	def peek(self):
		"""Peek the element at the front of the queue"""
		if len(self) == 0:
			return None
		else:
			return self._array[self._front]