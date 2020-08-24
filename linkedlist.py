"""LINKED LIST-BASED CONTAINERS

A linked list is a linear collection of data elements, in which each element
points to the next. It is a collection of nodes which together represent a 
sequence. In this library, each node contains an item and a reference to the 
next node in the sequence. 

    --------   --------   --------   --------   --------   --------
    | node |<--| node |<--| node |<--| node |<--| node |<--| node |
    --------   --------   --------   --------   --------   --------
       ^                                                       ^
      rear                                                   front

A linked list allows for efficient insertion or removal of elements at the 
front of the list, and efficient insertion at the rear of the list. A 
drawback is that only sequential access is possible while faster access (e.g.
random access) is not feasible. Arrays have better "cache" locality compared
to linked lists. 

For array-based counterparts, please see "containers" module. 

class | insertion | iterate | peek | removal
--------------------------------------------
Bag   | O(1)      | O(N)    | O(1) | N/A
Stack | O(1)      | O(N)    | O(1) | O(1)
Queue | O(1)      | O(N)    | O(1) | O(1)
--------------------------------------------

Here, an advantage of linked list-based container is that it has guaranteed 
O(1) performance for insertion & deletion compared to "amortized" O(1) 
performance provided by array implementation. 
"""
class ListNode:
	"""Node in a linked list

	Attributes:
		item: value of the current node 
		next: next node on the linked list
	"""
	def __init__(self, item=None, next=None):
		"""The constructor for Node class

		Parameters:
			item: value of the current node 
			next: next node on the linked list
		"""
		self.item = item 
		self.next = next

	def __str__(self):
		"""Print value of the node"""
		return str(self.item)


class Bag:
	"""A bag object is an unordered collection of elements. Bag operations
	include:
	1) adding an element to the bag (removing not allowed),
	2) testing if the bag is empty, 
	3) iterating through the bag. 

	        ++ -> ++ -> ++ ... ++
	        ^
	       head
	"""
	def __init__(self):
		"""Initialize a (None-terminated) linked list implementation of
		(empty) bag"""
		self._head = None #head pointer to linked list
		self._size = 0    #bag/linked list size

	def __iter__(self):
		"""Return an iterator to loop through the bag"""
		self._curr = self._head 
		return self

	def __len__(self):
		"""Return the size of the bag"""
		return self._size

	def __next__(self):
		"""Return the next element in the bag"""
		if self._curr is None:
			del self._curr
			raise StopIteration
		item = self._curr.item
		self._curr = self._curr.next
		return item 

	def __repr__(self):
		"""Print elements in the bag"""
		pass

	def add(self, item):
		"""Add an element to the bag"""
		self._head = ListNode(item, self._head)
		self._size += 1


class Stack:
	"""A stack object is an ordered collection of elements, which can be added
	or removed at "top". Stack operations include:
	1) pushing an item onto the stack, 
	2) poping an item off the stack, 
	3) checking if the stack is empty, 
	4) peeking the element on the top of the stack,
	5) iterating through the stack. 

	        ++ -> ++ -> ++ ... ++
	        ^
	       top

	Trying to pop an element off an empty stack is called "underflow".
	Whilst a stack is conceptually unbounded, it is desirable to fix the 
	maximum number of elements on a stack - thus excessive pushs will cause
	a stack to "overflow".

	Stacks are also known as LIFOs (last in, first out).
	"""
	def __init__(self):
		"""Initialize a (None-terminated) linked list implementation of 
		(empty) stack"""
		self._top  = None #top pointer to top of stack
		self._size = 0    #stack/linked list size

	def __iter__(self):
		"""Return an iterator to loop through stack"""
		self._curr = self._top
		return self

	def __len__(self):
		"""Return the stack size ~O(1)"""
		return self._size

	def __next__(self):
		"""Return next item on the stack"""
		if self._curr is None:
			raise StopIteration
		item = self._curr.item
		self._curr = self._curr.next 
		return item 

	def peek(self):
		"""Peek top item on stack"""
		if len(self) == 0:
			return None
		else:
			return self._top.item

	def pop(self):
		"""Pop item out of the stack"""
		if len(self) == 0:
			raise Exception("Stack underflow")
		item = self._top.item 
		self._top = self._top.next 
		self._size -= 1
		return item 

	def push(self, item):
		"""Push item onto the stack"""
		self._top = ListNode(item, self._top)
		self._size += 1


class Quque:
    """A queue object is an ordered collection of elements, which can be added
	at rear, and removed at front. Queue operations include:
	1) enqueuing an item onto the rear of the queue, 
	2) dequeuing an item from the front of the queue, 
	3) checking if the queue is empty or full, 
	4) peeking the element at the front of the queue.

	        ++ -> ++ -> ++ -> ... -> ++
	        ^                        ^
	      front                     rear

	Trying to dequeue an item off an empty queue is called "underflow".
	Whilst a queue is conceptually unbounded, it is desirable to fix the 
	maximum number of elements on a queue - thus excessive enqueues will cause
	the queue to "overflow".
	
	Queues are also known as FIFOs (first in, first out).
	"""
	def __init__(self):
		"""Initialize an array implementation of (empty) queue"""
		self._front = None #front pointer to 1st element (dequeue)
		self._rear  = None #rear pointer to last element (enqueue)
		self._size  = 0    #queue/linked list size

	def __iter__(self):
		"""Return an iterator to loop through the queue"""
		self._curr = self._front
		return self

	def __len__(self):
		"""Return the queue size ~ O(1)"""
		return self._size

	def __next__(self):
		"""Return the next item in the queue"""
		if self._curr is None:
			raise StopIteration
		item = self._curr.item
		self._curr = self._curr.next
		return item 

	def dequeue(self):
		"""Dequeue an item onto the front of the queue ~ O(1)"""
		if len(self) == 0:
			raise Exception("Queue underflow")
		item = self._front.item
		self._front = self._front.next
		self._size -= 1
		if len(self) == 0:
		#edge case - last node
			self._tail = None

	def enqueue(self, item):
		"""Enqueue an item from the rear of the queue ~ O(1)"""
		_2nd = self._rear
		self._rear = ListNode(item, None)	
	
		if len(self) == 0:
		#edge case - first node
			self._front = self._rear
		else:
			_2nd.next = self._rear 
		self._size += 1

	def peek(self):
		"""Peek the element at the front of the queue"""
		if len(self) == 0:
			return None
		else:
			return self._front.item