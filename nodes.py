"""NODES
This is a helper script which contains the defitions of all the nodes used in
this library. 

NodeLL  - node on linked list 
NodeBST - node on binary search tree

"""


"""Unlike linear data structures, trees can be traversed in different ways. 
Following are the generally used ways for traversing trees.
"""

from containers import Stack, Queue

class TreeNode:
	def __init__(self, value):
		self.val = value
		self.left = None
		self.right = None

# a naive binary search tree
tree = TreeNode(4)
tree.left = TreeNode(2)
tree.right = TreeNode(6)
tree.left.left = TreeNode(1)
tree.left.right = TreeNode(3)
tree.right.left = TreeNode(5)
tree.right.right = TreeNode(7)


def traverse(root, method="dfs", order="in"):
	"""tree traversal wrapper function
	
	Arguments:
	root   -- root of binary tree
	method -- bfs (breadth-first search) or dfs (depth-first search)
	order  -- inorder/preorder/postorder (only for dfs)
	"""
	if method.lower() == "bfs":
		_bfs(root)
	elif order[:2].lower() == "in":
		_dfs_in(root)
	elif order[:3].lower() == "pre":
		_dfs_pre(root)
	elif order[:4].lower() == "post":
		_dfs_post(root)
	else:
		raise Exception(f'Invalid arguments {method} and {order}')


def _dfs_recur(root):
	"""recursive depth-first traversal of a binary tree"""
	if root is None: return 
    #   inorder traversal : left-node-right
	#  preorder traversal : node-left-right
	# postorder traversal : left-right-node
	traverse(root.left)
	print(root.val, end=" ")
	traverse(root.right)


def _dfs_in(root):
	"""inorder depth-first traversal of a binary tree"""
	node = root 
	stack = Stack()
	while node or stack:
		if node: 
		# go-left
			stack.push(node)
			node = node.left 
			continue
		node = stack.pop() # go-back
		print(node.val, end=" ")
		node = node.right  # go-right

"""
#GENERATOR 
def inorder(node):
    if node:
        yield from inorder(node.left)
        yield node.val
        yield from inorder(node.right)
"""		


def _dfs_pre(root):
	"""preorder depth-first traversal of a binary tree"""
	stack = Stack()
	stack.push(root)
	while stack:
		node = stack.pop()
		if node:
			print(node.val, end=" ")
			stack.push(node.right)
			stack.push(node.left)


def _dfs_post(root):
	"""postorder depth-first traversal of a binary tree"""
	stack = Stack()
	value = Stack()

	stack.push(root)

	while stack:
		node = stack.pop()
		if node:
			stack.push(node.left)
			stack.push(node.right)
			value.push(node.val)

	while value:
		print(value.pop(), end=" ")


def _bfs(root):
	"""breadth-first traversal of a binary tree"""
	queue = Queue()
	queue.enqueue(root)
	while queue:
		node = queue.dequeue()
		if node is not None:
			print(node.val, end=" ")
			queue.enqueue(node.left)
			queue.enqueue(node.right)