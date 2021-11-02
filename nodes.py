"""NODES
This is a helper script which contains the defitions of all the nodes used in
this library. 

NodeLL  - node on linked list 
NodeBST - node on binary search tree

"""


"""Unlike linear data structures, trees can be traversed in different ways. 
Following are the generally used ways for traversing trees.
"""

from collections import deque

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

# a naive binary search tree
tree = TreeNode(4)
tree.left = TreeNode(2)
tree.right = TreeNode(6)
tree.left.left = TreeNode(1)
tree.left.right = TreeNode(3)
tree.right.left = TreeNode(5)
tree.right.right = TreeNode(7)


def dfs(root):
    """Recursively depth-first traverse a binary tree."""
    if not root: return 
    #   inorder traversal : left-node-right
    #  preorder traversal : node-left-right
    # postorder traversal : left-right-node
    yield from dfs(root.left)
    yield root.val
    yield from dfs(root.right)


def inorder(root):
    """Inorder depth-first traverse a binary tree."""
    ans = []
    node, stack = root, []
    while node or stack:
        if node: # go-left
            stack.append(node)
            node = node.left 
        else: 
            node = stack.pop() # go-back
            ans.append(node.val)
            node = node.right  # go-right
    return ans 

"""
#GENERATOR 
def inorder(node):
    if node:
        yield from inorder(node.left)
        yield node.val
        yield from inorder(node.right)
"""     

def preorder(root):
    """Preorder depth-first traverse a binary tree."""
    ans = []
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            ans.append(node.val)
            stack.extend([node.right, node.left])
    return ans 


def postorder(root):
    """Postorder depth-first traverse a binary tree."""
    ans = []
    node, stack = root, []
    while node or stack: 
        if node: 
            if node.right: stack.append(node.right)
            stack.append(node)
            node = node.left
            continue
        node = stack.pop()
        if stack and stack[-1] == node.right: 
            stack.pop()
            stack.append(node)
            node = node.right
        else:
            ans.append(node.val)
            node = None
    return ans 


def postorder(root):
    """Postorder depth-first traverse a binary tree."""
    ans = []
    node, stack = root, []
    prev = None 
    while node or stack:
        if node: 
            stack.append(node)
            node = node.left 
        else: 
            node = stack[-1] 
            if node.right and node.right != prev: node = node.right 
            else: 
                ans.append(node.val) 
                stack.pop() 
                prev = node 
                node = None
    return ans 


def bfs(root):
    """breadth-first traversal of a binary tree"""
    ans = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            ans.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
    return ans 


if __name__ == "__main__":
    print(inorder(tree))
    print(preorder(tree))
    print(postorder(tree))
    print(bfs(tree))

    for x in dfs(tree): print(x) # from generator 