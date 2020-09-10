"""A trie (aka prefix tree) is one type of search tree — an tree data structure 
used to store associative array where the keys are strings. Unlike BST, no node 
in the tree stores the key associated with that node; instead, its position in 
the tree defines the key with which it is associated; i.e., the value of the 
key is distributed across the structure. All the descendants of a node have a 
common prefix of the string associated with that node, and the root is 
associated with the empty string."""


class TrieNode:
    """Node on trie"""
    def __init__(self):
        self.data = [None]*26 #lowercase letter only
        self.word = False     #true if a word terminates here 
        

class Trie:
    """Trie data structure via trie node class."""

    def __init__(self):
        """Initialize your data structure here."""
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Inserts a word into the trie."""
        node = self.root
        for i in (ord(x) - 97 for x in word): 
            if not node.data[i]: node.data[i] = TrieNode()
            node = node.data[i]
        node.word = True
        
    def _traverse(self, word): 
        """Traverse the trie to find word."""
        node = self.root
        for i in (ord(x)-97 for x in word):
            if not node.data[i]: return None
            node = node.data[i]
        return node
        
    def search(self, word: str) -> bool:
        """Returns if the word is in the trie."""
        node = self._traverse(word)
        return node.word if node else False 
        
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self._traverse(prefix)


class ToyTrie:
    """This ToyTrie implementation is primarily for interview purpose. Here, 
    the trie is implemented via nested dictionaries."""

    def __init__(self):
        """Initialize the trie by defining the root."""
        self.root = {}

    def insert(self, word: str) -> None:
        """Insert the word to the trie."""
        node = self.root
        for letter in word: 
            node = node.setdefault(letter, {}) # move along the trie
        node["#"] = True #sentinel 

    def search(self, word: str) -> bool:
        """Return True if word can be found on the trie."""
        node = self.root
        for letter in word:
            if letter not in node: return False 
            node = node[letter]
        return node.get("#", False)

    def startsWith(self, prefix: str) -> bool:
        """Return True if prefix can be found on the trie."""
        node = self.root
        for letter in prefix:
            if letter not in node: return False
            node = node[letter]
        return True 