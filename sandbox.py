from math import inf
from typing import List

class SegTree: 
    """A segment tree, aka a statistic tree, is a tree data structure used for 
    storing information about intervals. It allows querying which of the stored 
    segments contain a given point."""

    def __init__(self, arr: List[int]): 
        """Return """
        self.n = len(arr)
        self.data = [0]*(4*self.n)
        self._build(arr, 0, 0, self.n)

    def _build(self, arr: List[int], k: int, lo: int, hi: int) -> None: 
        """Return """
        if lo+1 == hi: 
            self.data[k] = arr[lo]
            return 
        mid = lo + hi >> 1
        self._build(arr, 2*k+1, lo, mid)
        self._build(arr, 2*k+2, mid, hi)
        self.data[k] = min(self.data[2*k+1], self.data[2*k+2])

    def update(self, idx: int, val: int, k: int = 0, lo: int = 0, hi: int = 0) -> None:
        if not hi: hi = self.n
        if lo+1 == hi: 
            self.data[k] = val 
            return 
        mid = lo + hi >> 1
        if idx < mid: 
            self.update(idx, val, 2*k+1, lo, mid) 
        else: 
            slef.update(idx, val, 2*k+2, mid, hi)
        self.data[k] = min(self.data[2*k+1], self.data[2*k+2])

    def query(self, qlo: int, qhi: int, k: int = 0, lo: int = 0, hi: int = 0) -> int: 
        if not hi: hi = self.n
        """Return """
        if qlo <= lo and hi <= qhi: return self.data[k] # total overlap 
        if qhi <= lo or  hi <= qlo: return inf # no overlap 
        mid = lo + hi >> 1 # partial overlap 
        return min(self.query(qlo, qhi, 2*k+1, lo, mid), self.query(qlo, qhi, 2*k+2, mid, hi))


arr = [1,3,7,5,8,6,4,2]
tree = SegTree(arr)
print(tree.query(4, 7))