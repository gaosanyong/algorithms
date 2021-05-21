"""BALANCED SEARCH TREES

2-3 TREE
2-node | one key, two children
3-node | two keys, three children 
perfect balance - every path from root to None has same length
symmetric order - inorder traversal yields keys in ascending order 
implementation is complicated 

Red-Black BSTs
Represent 2-3 tree as BST
Use "internal" left-leaning links as "glue" for 3-nodes

A left-leaning red-black (LLRB) BST is A BST such that:
* no node has two red links connected to it;
* every path from root to null link has the same number of black links;
* red links lean left.

A red-black tracks every simple path from a node to a descendant leaf with the same number of black nodes. 

B-tree
* at least 2 key-link pairs at root;
* at least M/2 key-link pairs in other nodes;
* external nodes contain client keys;
* internal nodes contain copies of keys to guide search. 

Variants: B+tree, B*tree, B#tree, ...

2d-tree 

recursively partition plan into two half planes


"""

class LLRB:
	def __init__(self):
		pass

	def __len__(self):
		pass

	def get(self, key):
		node = self.root


	def rotateleft(self, node):
		"""
		Rotate to the left inside 3-node to have left-leaning structure

		node                      temp
		    \                    /
		     temp     =>     node
		    /                    \
		child                     child

		LLRB elementary operation
		"""
		assert self.isred(node.right)
		temp = node.right
		node.right = temp.left
		temp.left = node
		temp.color = node.color
		node.color = RED
		return temp 

	def rotateright(self, node):
		"""
		Rotate to the right within 3-node (temporarily)

		       |              |
		     node           temp
		    /                   \
		temp          =>         node
		    \                   /
		     child         child

		LLRB elementary operation
		"""
		assert self.isred(node.left)
		temp = node.left
		node.left = temp.right
		temp.right = node 
		temp.color = node.color
		node.color = RED
		return temp 

	def flipcolor(self, node):
		"""
		Split 3-node into 2-nodes

		LLRB elementary operation
		"""
		assert not self.isred(node)
		assert self.isred(node.left)
		assert self.isred(node.right)
		node.color = RED
		node.left.color = BLACK 
		node.right.color = BLACK

	def _put(self, node, key, val):
		"""
		right-leaning 3-node:
		rotate left into left-leaning 3-node
		4-node:
		rotate right into a geometry for split
		split 
		"""
		if node is None:
			return NodeBST(key, val, RED)

		if key < node.key:
			node.left = self._put(node.left, key, val)
		elif key > node.key:
			node.right = self._put(node.right, key, val)
		else:
			node.val = val 

		#rotate left right-leaning 3-node into left-leaning
		if isred(node.right) and not isred(node.left):
			node = rotateleft(node)
		#rotate right 4-node into a temporary position for split
		if isred(node.left) and isred(node.left.left):
			node = rotateright(node) #right
		#split temporary 4-node into three 2-nodes
		if isred(node.left) and isread(node.right):
			flipcolor(node)

		return node 


	def moveRedLeft(self, node): 
		""""""
		flipcolor(node)
		if self.isRed(node.right.left): 
			node.right = self.rotateRight(node.right)
			node = self.rotateLeft(node)
		return node 


	def moveRedRight(self, node): 
		""""""
		flipcolor(node)
		if not self.isRed(node.left.left): 
			node = self.rotateRight(node)
		return node 


	def deleteMin(self): 
		""""""
		if not self.isRed(self.root.left) and not self.isRed(self.root.right): 
			self.root.color = RED
		self.root = self._deleteMin(self.root)
		if not self.isEmpty(): self.root.color = BLACK 


	def _deleteMin(self, node): 
		""""""
		if node.left is None: return None
		if not self.isRed(node.left) and not self.isRed(node.left.left): 
			node = self.moveRedLeft(node)
		node.left = _deleteMin(node.left)
		return self.balance(node)


	def _delete(self, node, key):
		"""LLRB deletion"""
		if key < node.key: 
			if not self.isRed(node.left) and not self.isRed(node.left.left): 
				node = self.moveRedLeft(node)
			node.left = self._delete(node.left, key)
		else: 
			if self.isRed(node.left): 
				node = self.rotateRight(node)
			if key == node.key and node.right is None: 
				return None 
			if not self.isRed(node.right) and not self.isRed(node.right.left): 
				node = self.moveRedRight(node) 
			if key == node.key: 
				node.val = self.get(node.right, self.getMin(node.right))
				node.key = self.getMin(node.right).key 
				node.right = self.deleteMin(node.right) 
			else: 
				node.right = self._delete(node.right, key) 
		return self.balance(node)


class BTree:
	"""B-tree
	
	Bayer-McCreight 1972 
	"""
	pass 


class AVLTree: 
	pass 