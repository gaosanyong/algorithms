"""INTERVIEW QUESTIONS"""

"""BIT OPERATIONS 

n & n-1 # unset last set bit 
n & -n # retain last set bit 
"""


"""
Fibonacci numbers were introduced by Italian mathematician Fibonacci in his 
1202 book Liber Abaci as

F(n) = F(n-1) + F(n-2)

where F(0) = 0 and F(1) = 1. For example, 

  index : 0, 1, 2, 3, 4, 5, 6, 7,  8,  9,  10, 11, 12,  13, ... 
numbers : 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...

The nth Fibonacci number can be computed from its definition as O(N) algorithm.

In addition, there are 2 known formula which can provide O(1) algorithm. 
phi = (sqrt(5) + 1)/2 (golden ratio)
F(n) = (phi**n - (1/phi)**n)/sqrt(5) or F(n) = [phi**n/sqrt(5)]
"""

# O(N) algorithms 

#naive recursive solution | time ~ O(2**n)
def fib(n):
	"""nth fibonacci number (recursive)"""
	if n == 0 or n == 1: return n #base case
	return fib(n-1) + fib(n-2)

#memoized solution I | time ~ O(n)
memo = dict()
def fib(n):
    """nth fibonacci number (recursive)"""
    if n in memo: return memo[n]
    if n == 0 or n == 1: 
        return n
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

#memoized solition II (some interviewers don't like global variables)
def fib(n, memo=dict()):
    if n in memo: return memo[n]
    if n == 0 or n == 1: return n
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

#memoized solution III
from functools import lru_cache
@lru_cache(None)
def fib(n):
    if n == 0 or n == 1: return n
    return fib(n-1) + fib(n-2)

#bottom-up dynamic programming
def fib(n):
	"""nth fibonacci number (iterative)"""
	a, b = 0, 1
	for _ in range(n): a, b = b, a+b
	return a 

def fib(n, a=0, b=1):
	"""nth fibonacci number (tail-recursive)"""
	if n == 0: return a 
	return fib(n-1, b, a+b)

def fib():
	"""fibonacci number generator"""
	a, b = 0, 1
	while True:
		yield a
		a, b = b, a+b

# O(logN) algorithms

# O(1) algorithms

from math import sqrt 
def fib(n):
    """fibonacci ~ O(1)
    Binet formula (1843)
    """
    phi = (sqrt(5) + 1)/2
    return (phi**n - (phi-1)**n)/sqrt(5)

def fib(n):
    """fibonacci ~ O(1)
    A simpler closed form formula
    """
    phi = (sqrt(5) + 1)/2
    return round(phi**n /sqrt(5))

# subsetsfrom math import sqrt 

def fib(n):
    """fibonacci ~ O(1)"""
    return ((sqrt(5)+1)/2)**n /sqrt(5)


# Babylonian square-root algorithm 
# Given N, find its square root
# Algo:
# 1) make an initial guess x
# 2) update the guess as x = (x + N/x)/2 until convergence 

def subsets(self, nums):
    """Power set algorithm
    1) set size is n, power set size is 2**n;
    2) loop through power set i:0 -> 2**n-1,
       loop through set j:0 -> n-1
       
    set = [a,b,c] 
    000  []
    001  [a]
    010  [b]
    011  [a,b]
    100  [c] 
    101  [a, c]
    110  [a, b] 
    111  [a, b, c]
    """
    nums = sorted(nums)
    
    n = len(nums) #set size 
    sets = []
    for i in range(1 << n): #1 << n is power set size 
    #retain jth element if match
        sets.append([nums[j] for j in range(n) if (i & (1 << j))]) 
        
    return sets 


def subsets(self, nums):
    """tail recursive"""
    
    nums = sorted(nums)
    
    subsets_ = []
    def tail(nums, curr=0, subset=[]):
        """"""
        if curr == len(nums):
            subsets_.append(subset)
            return 
        tail(nums, curr+1, subset[:])
        tail(nums, curr+1, subset[:] + [nums[curr]])
    tail(nums)
    
    return subsets_

#check palindrome string
def is_palin(string):
    return all(string[i] == string[~i] for i in range(len(string)//2+1))

def is_palin(string):
    lo, hi = 0, len(string) - 1
    while lo < hi and string[lo] == string[hi]:
        lo += 1
        hi -= 1
    return lo >= hi


def boyer_moore(pattern, text):
    """Boyer-Moore string search algorithm"""
    m, n = len(pattern), len(text)
    jump = {}
    for i, c in enumerate(pattern):
        jump[c] = i 

    offset = 0
    while offset < n-m:
        skip = 0
        for j in reversed(range(m)):
            if text[offset+j] != pattern[j]:
                skip = max(1, j - jump.get(pattern[j], -1))
                break 
        if skip == 0: return True
        offset += skip
    return False #not found 


def rabin_karp(pattern, text):
    """Rabin Karp string search algorithm (Monte Carlo)"""
    R, Q = 128, 997
    hp = ht = 0 
    rm = 1/R
    for p, t in zip(pattern, text):
        hp = (hp * R + ord(p)) % Q
        ht = (ht * R + ord(t)) % Q 
        rm = rm * R % Q 
    if hp == ht: return True 

    m, n = len(pattern), len(text)
    for i in range(m, n):
        ht = (ht + Q - ord(text[i-m])) % Q
        ht = (ht + ord(text[i])) % Q 
        if ht == hp: return True 

    return False 


def KMP(pattern, text):
    """Knuth-Morris-Pratt algorithm (1977) for string search
    When a mismatch occurs, the pattern itself embodies sufficient info to
    determine where the next match could begin, thus bypassing re-examination 
    of previously matched characters
    """
    
    """building longest prefix-suffix (lps) array
    lps[i] stores length of maximum proper prefix which is also a suffix in 
    pattern[:i+1] (note lps[0] is always 0). A proper prefix is prefix not 
    whole string. For example, proper prefixes of "ABC" include "", "A", "AB" 
    but not "ABC". 
    
    For example, "aaab" results in an lps of [0,1,2,0]. 
    """
    lps = [0] #longest prefix-suffix array
    k = 0
    for i in range(1, len(pattern)):
        while k and pattern[k] != pattern[i]: 
            k = lps[k-1]
        if pattern[k] == pattern[i]: k += 1
        lps.append(k)
    
    """Given an lps array which indicates where to start a new match in the 
    event of a mismatch, we continue searching from pattern[lps[j-1]]."""
    k = 0
    for i in range(len(text)): 
        while k and pattern[k] != text[i]:
            k = lps[k-1]
        if pattern[k] == text[i]: k += 1
        if k == m: return i - m + 1
    return -1 
    

def dfs_recursive(node):
    if node:
        #do something
        dfs(node.left)
        dfs(node.right)

def dfs_preorder(root):
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            #do something
            stack.push(node.right)
            stack.push(node.left)

from collections import deque
def bfs(root):
    """breadth first search implemented using while loop"""
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            #do something
            queue.push(node.left)
            queue.push(node.right)

def bfs(root):
    """breadth first search implemented using for loop"""
    queue = [root]
    for node in queue:
        if node:
            #do something
            queue.push(node.left)
            queue.push(node.right)            
    

def choose(n, k):
    """combinatorics n choose k"""
    ans = 1
    for i in range(k):
        ans *= n - i
        ans //= i + 1
    return ans 


def bsort(A):
    """bucket sort O(N)"""
    count = [0]*1000
    for x in A: count[x-1] += 1
    ans = []
    for i, x in enumerate(count, 1):
        if x: ans.extend([i]*x)
    return ans 


def qsort(nums: List[int]) -> List[int]:
    """Quick sort O(NlogN)"""
    shuffle(nums) # statistical guarantee of O(NlogN)
    
    def part(lo, hi): 
        """Return a random partition of nums[lo:hi]."""
        i, j = lo+1, hi-1
        while i <= j: 
            if nums[i] < nums[lo]: i += 1
            elif nums[j] > nums[lo]: j -= 1
            else: 
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        nums[lo], nums[j] = nums[j], nums[lo]
        return j
        
    def sort(lo, hi): 
        """Sort subarray nums[lo:hi] in place."""
        if lo + 1 >= hi: return 
        mid = part(lo, hi)
        sort(lo, mid)
        sort(mid+1, hi)
        
    sort(0, len(nums))
    return nums

### reproducing product functionality 
### product(["abc", "def", "ghi"])
def op(x, y):
    """cartesian product"""
    return [xx + yy for xx in x for yy in y]

product = lambda x: reduce(op, x)

def product(*args):
    """A naive implementation of python product function"""
    if not args: return [[]]
    return [[x]+y for x in args[0] for y in product(*args[1:])]

### combinations 
def combinations(x, n):
    if not n or len(x) < n: return [""]
    if len(x) == n: return [x]
    return [x[0] + y for y in combinations(x[1:], n-1)] + combinations(x[1:], n)
    
### permutations
def permutations(x):
    """Return all permutations of x"""

    def fn(i):
        if i == len(x): ans.append(x.copy())
        for k in range(i, len(x)):
            x[i], x[k] = x[k], x[i]
            fn(i+1)
            x[i], x[k] = x[k], x[i]

    ans = []
    fn(0)
    return ans 


def permutations(x):
    """Heap's algorithm"""

    def fn(i):
        if i == len(x): ans.append(x.copy())
        for k in reversed(range(i, len(x))):
            fn(i+1)
            if (len(x)-i) & 1: nums[i], nums[-1] = nums[-1], nums[i]
            else: nums[i], nums[k] = nums[k], nums[i]

    ans = []
    fn(0)
    return ans 

"""compute sqrt(2) using Newton Raphson
x = x - f(x)/df(x)
where f(x) = x**2 - 2 in this case
"""

def my_sqrt(num, epsilon=1e-6, maxiter=1e6):
    """Return square root of num using Newton Raphson method"""
    x0, x1 = 0, 1
    cnt = 0
    while abs(x1 - x0) > epsilon: 
        x0, x1 = x1, 0.5*(x1 + num/x1)
        cnt += 1
        if cnt == maxiter: raise Exception("Max iteration reached")
    return x1


def bfs(s):
    """mit 6.006 by Erik Demaine"""
    level = {s: 0}
    parent = {s: None}
    i = 0 
    frontier = [s]
    while frontier:
        next = []
        for u in frontier: 
            for v in adj[u]:
                if v not in level:
                    level[v] = i
                    parent[v] = u
                    next.append(v)
        i += 1


def bisect_left(a, x, lo=0, hi=None):
    """bisection search (left)"""
    if hi is None: hi = len(a)
    while lo < hi: 
        mid = (lo + hi)//2
        if a[mid] < x: lo = mid + 1
        else: hi = mid 
    return lo


def bisect_right(a, x, lo=0, hi=None):
    """bisection search (right)"""
    if hi is None: hi = len(a)
    while lo < hi: 
        mid = (lo + hi)//2
        if a[mid] <= x: lo = mid + 1
        else: hi = mid
    return lo 


def date2num(y, m, d):
    """A magical formula to convert date to num such that 
    the difference of two dates reflects the days in between"""
    if m < 3: y, m = y-1, m+12
    return 365*y+y//4+y//400-y//100+d+(153*m+8)//5


class Fenwick: 
    """Fenwick tree for range sum query (RSQ).
    Fenwick tree (Peter Fenwick 1994) aka binary indexed tree (BIT) is a 
    tree data structure implemented via array to efficiently compute prefix 
    sums."""

    def __init__(self, n: int):
        """Initialize a Fenwick tree with n values."""
        self.tree = [0]*(n+1)

    def query(self, k: int) -> int: 
        """Return the prefix sum aka sum(nums[:k+1])."""
        k += 1
        ans = 0
        while k:
            ans += self.tree[k]
            k -= k & -k # unset last set bit 
        return ans

    def add(self, k: int, x: int) -> None: 
        """Add the kth element with value x to Fenwick tree."""
        k += 1
        while k < len(self.tree): 
            self.tree[k] += x # add on top of existing value
            k += k & -k 


class Fenwick: 
    """Fenwick tree for range max query (RMQ)."""
    def __init__(self, n: int): 
        """Initialize a Fenwick tree with n values."""
        self.data = [0]*(n+1)

    def query(self, k: int) -> int: 
        """Return prefix max aka max(nums[:k+1])."""
        k += 1
        ans = 0 
        while k:
            ans = max(ans, self.data[k])
            k -= k & (-k)
        return ans 
            
    def update(self, k: int, x: int) -> None: 
        """Update the kth element with value x to Fenwick tree."""
        k += 1
        while k < len(self.data): 
            self.data[k] = max(self.data[k], x) # update to max
            k += k & (-k)


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
        if idx < mid: self.update(idx, val, 2*k+1, lo, mid) 
        else: self.update(idx, val, 2*k+2, mid, hi)
        self.tree[k] = min(self.tree[2*k+1], self.tree[2*k+2])

    def query(self, qlo: int, qhi: int, k: int = 0, lo: int = 0, hi: int = 0) -> int: 
        """Query value from qlo (inclusive) and qhi (exclusive)."""
        if not hi: hi = self.n
        if qlo <= lo and hi <= qhi: return self.tree[k] # total overlap 
        if qhi <= lo or  hi <= qlo: return inf # no overlap 
        mid = lo + hi >> 1 # partial overlap 
        return min(self.query(qlo, qhi, 2*k+1, lo, mid), self.query(qlo, qhi, 2*k+2, mid, hi))


class Trie:
    """Trie aka digital tree or prefix tree is a tree data structure to 
    efficiently store strings. This implementation uses nested dictionaries."""

    def __init__(self):
        """Initialize the trie by defining the root."""
        self.root = {}

    def insert(self, word: str) -> None:
        """Insert the word to the trie."""
        node = self.root
        for letter in word: 
            node = node.setdefault(letter, {}) # move along the trie
        node["#"] = word #sentinel 

    def search(self, word: str) -> bool:
        """Return True if word can be found on the trie."""
        node = self.root
        for letter in word:
            if letter not in node: return False 
            node = node[letter]
        return node.get("#", False)


class UnionFind:
    """UnionFind aka disjoint-set or disjoint-set union is a data structure 
    that stores a collection of disjoint sets."""

    def __init__(self, N: int):
        self.count = N               # count of disjoint components
        self.parent = list(range(N)) # parent array (to reflect subsets)
        self.rank = [1] * N          # size of subtree

    def find(self, p: int, halving: bool=True) -> int:
        if p != self.parent[p]:
            self.parent[p] = self.find(self.parent[p]) # path compression
        return self.parent[p]

    def union(self, p: int, q: int, ranking: bool=True) -> bool:
        prt, qrt = self.find(p), self.find(q)
        if prt == qrt: return False #already linked
        if ranking and self.rank[prt] > self.rank[qrt]: 
            prt, qrt = qrt, prt #p-tree is smaller 
        self.count -= 1
        self.parent[prt] = qrt #link p-tree to q-tree
        self.rank[qrt] += self.rank[prt] #update q-tree size
        return True 


# Cycle detection for undirected graph utilizes Union-Find data structure.

def tpsort(graph, indeg):
    """Topological sort for digraph via Kahn's algorithm."""
    stack = [n for n in graph if indeg[n] == 0]
    ans = []
    while stack: 
        n = stack.pop()
        ans.append(n)
        for nn in graph.get(n, []): 
            indeg[nn] -= 1
            if indeg[nn] == 0: stack.append(nn)
    if len(ans) == len(indeg): return ans
    return [] # cycle detected 


def tpsort(graph):
    """Topological sort for digraph via tri-color encoding."""
        
    def dfs(n):
        """Return True if a cycle is detected."""
        if visited[n]: return visited[n] == -1
        visited[n] = -1 # GRAY (temporary mark)
        for nn in digraph.get(n, []):
            if visited[nn] != 1 and dfs(nn): return True 
        ans.append(n)
        visited[n] = 1 # BLACK (permanent mark)
        return False 
    
    ans = []
    visited = [0]*len(graph) # WHITE
    for n in range(len(graph)): 
        if dfs(n): return [] 
    ans.reverse()
    return ans 


def tarjan(n: int, connections: List[List[int]]) -> List[List[int]]:
    """Tarjan's algo to find bridges (critical edges) in a graph."""
    graph = {} # graph as adjacency list 
    for u, v in connections: 
        graph.setdefault(u, []).append(v)
        graph.setdefault(v, []).append(u)
    
    def dfs(x, p, step): 
        """Traverse the graph and collect bridges using Tarjan's algo."""
        disc[x] = low[x] = step
        for xx in graph.get(x, []): 
            if disc[xx] == inf: 
                step += 1
                dfs(xx, x, step)
                low[x] = min(low[x], low[xx])
                if low[xx] > disc[x]: ans.append([x, xx]) # bridge
            elif xx != p: low[x] = min(low[x], disc[xx])
    
    ans = []
    low = [inf]*n
    disc = [inf]*n
    
    dfs(0, -1, 0)
    return ans 


def hasEulerianPath(graph): 
    """Return True if given graph has an Eulerian path."""
    indeg = [0]*len(graph)
    outdeg = [0]*len(graph)
    for u, nodes in graph: 
        outdeg[u] = len(nodes)
        for v in nodes: indeg[v] += 1
    start = end = 0 
    for x in range(len(graph)): 
        if abs(indeg[x] - outdeg[x]) > 1: return False 
        if outdeg[x] - indeg[x] == 1: start += 1
        elif indeg[x] - outdeg[x] == 1: end += 1
    return start == end == 0 or start == end == 1


def hierholzer(graph):
    """Return an Eulerian path via Hierholzer algo"""
    ans = []

    def fn(x): 
        """Return Eulerian path via dfs."""
        while graph[x]: fn(graph[x].pop()) 
        ans.append(x)

    ans.reverse()
    return ans 


def qksort(nums: List[int]) -> List[int]:
    """Quick sort given array (in-place)."""
    shuffle(nums)                
        
    def sort(lo, hi): 
        """Sort nums[lo:hi] via quick sort."""
        if lo + 1 >= hi: return 
        i, j = lo+1, hi-1
        while i <= j: 
            if nums[i] < nums[lo]: i += 1
            elif nums[j] > nums[lo]: j -= 1
            else: 
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        nums[lo], nums[j] = nums[j], nums[lo]
        sort(lo, j)
        sort(j+1, hi)
        
    sort(0, len(nums))
    return nums


def mgsort(nums: List[int]) -> List[int]:
    """Merge sort given array (in-place)."""
    
    def sort(nums, aux, lo, hi): 
        """Sort nums via merge sort."""
        if lo+1 >= hi: return 
        mid = lo + hi >> 1
        sort(aux, nums, lo, mid)
        sort(aux, nums, mid, hi)
        i, j = lo, mid
        for k in range(lo, hi): 
            if j >= hi or i < mid and aux[i] < aux[j]: 
                nums[k] = aux[i]
                i += 1
            else: 
                nums[k] = aux[j]
                j += 1
    
    sort(nums, nums.copy(), 0, len(nums))
    return nums 


def manacher(s: str) -> str:               
    """Return longest palindromic substring via Manacher's algo."""
    ss = "#" + "#".join(s) + "#" # augmented string (even-length palindromes)
    n = len(ss)
    hlen = [0] * n # half-length
    center = right = 0
    for i in range(n):
        if i < right: hlen[i] = min(right-i, hlen[2*center-i])
        while 0 <= i-1-hlen[i] and i+1+hlen[i] < len(ss) and ss[i-1-hlen[i]] == ss[i+1+hlen[i]]: hlen[i] += 1
        if right < i+hlen[i]: center, right = i, i+hlen[i]
    xx, ii = max((x, i) for i, x in enumerate(hlen))
    return s[(ii-xx)//2 : (ii+xx)//2]


def fibonacci(n): 
    """Return nth Fibonacci number using Binet formula"""
    phi = (1 + sqrt(5))/2
    return round((phi**n - (1-phi)**n)/sqrt(5))


if __name__ == "__main__":

    print(date2num(2020, 1, 15) - date2num(2019, 12, 31))

    # Fenwick tree
    nums = [1, 7, 3, 0, 5, 8, 3, 2, 6, 2, 1, 1, 4, 5]
    fen = Fenwick(len(nums))
    for i, x in enumerate(nums): fen.add(i, x) 

    print(fen.sum(5))  # 16
    print(fen.sum(10)) # 37
    print(fen.sum(14)) # 48