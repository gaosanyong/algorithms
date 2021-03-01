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
* every path from root to null link has the same number of black linkts;
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

		if isred(node.right) and not isred(node.left):
		#rotate left right-leaning 3-node into left-leaning
			node = rotateleft(node)
		if isred(node.left) and isred(node.left.left):
		#rotate right 4-node into a temporary position for split
			node = rotateright(node) #right
		if isred(node.left) and isread(node.right):
		#split temporary 4-node into three 2-nodes
			flipcolor(node)

		return node 

	def _delete(self, key):
		"""LLRB deletion"""
		pass 


class BTree:
	"""B-tree
	
	Bayer-McCreight 1972 
	"""
	pass 


class AVLTree: 
	pass 