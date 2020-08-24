"""screen scraping"""
import requests 

def stock_quote(ticker="AAPL", source="yahoo"):
	"""Screen scrape stock quote from given source

	Arguments:
	ticker -- stock ticker, e.g. AAPL for Apple
	source -- source of information, e.g. yahoo for Yahoo! Finance
	"""
	mapping = {"yahoo": f"https://finance.yahoo.com/quote/{ticker}?p={ticker}&.tsrc=fin-srch"}
	url = mapping[source.lower()]
	response = requests.get(url)
	if response.status_code != 200: raise ConnectionError

	content = response.text	
	price = content.find("regularMarketPrice")
	lo = content.find("raw", price)
	hi = content.find("fmt", price)
	if min(price, lo, hi) == -1: raise ValueError("Price not found")

	return float(content[lo+5:hi-2])


# if __name__ == "__main__":
# 	tickers = ["AAPL", "GOOG", "MSFT", "NFLX"]
# 	for ticker in tickers:
# 		print(ticker, stock_quote(ticker))


class Point2:
	"""2-D point"""
	def __init__(self, x, y):
		self.val = (x, y)

	def __sub__(self, other):
		return (self.val[0] - other.val[0], self.val[1] - other.val[1])
		

from math import atan2, pi
from containers import Stack 

def cvxhull(points):
	"""Return convex hull of given 2d points using Graham scan algorithm

	Arguments:
	- points: a list of 2-d points
	
	Graham scan algorithm:
	- choose point p with smallest (or largest) y coordinate
	- sort points by polar angle with p to get simple polygon
	- consider points in order, and discard those that would create a clockwise turn
	"""
	idx = max(range(len(points)), key = lambda i: points[i][0]) #point with largest x coordinate
	pivot = points.pop(idx)
	#sort by polar angle in ascending order
	points.sort(key = lambda x: (atan2(x[1] - pivot[1], x[0] - pivot[0]) + 2*pi) % 2*pi )
	print(pivot)
	print(points)

	stack = []
	stack.push(pivot)
	for point in points:
		while len(stack) > 1: 
			pivot = stack.pop()	
			fixed = stack[-1] #peek
			if not _clockwise(fixed, pivot, point): 
				stack.push(pivot)
				break 
		stack.push(point)
	return stack 


def _clockwise(pnt1, pnt2, pnt3):
	"""Return True if pnt2->pnt2->pnt3 is clockwise"""	
	vec1 = (pnt2[0] - pnt1[0], pnt2[1] - pnt1[1])
	vec2 = (pnt3[0] - pnt2[0], pnt3[1] - pnt2[1])
	return vec1[0] * vec2[1] - vec1[1] * vec2[0] < 0


class HamiltonPath:
	"""Hamilton path (NP-complete)"""
	def __init__(self, graph):
		""""""
		self.count = 0
		self.marked = [False] * len(graph)
		for v in graph.V():
			self.dfs(graph, v, 1)

	def dfs(self, graph, v, depth):
		"""Depth-first search starting at v

		depth -- length of current path (depth of recursion)
		"""
		self.marked[v] = True
		if (depth == graph.V()): self.count += 1 #found one
		for w in graph.adj(v):
			if not self.marked[w]: self.dfs(graph, w, depth+1) #backtrack if w is already part of path
		self.marked[v] = False #clean up



if __name__ == "__main__":
	file = "data/cvxhull.txt"
	with open(file, "r") as fh:
		n = int(fh.readline())
		points = [None]*n
		for i in range(n):
			points[i] = tuple(int(x) for x in fh.readline().split())
	hull = cvxhull(points)
	print(hull)
	print(zip(*hull))


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        """"""
        oldColor = image[sr][sc]
        image[sr][sc] = newColor
        if sr > 0 and image[sr-1][sc] == oldColor: self.floodFill(image, sr-1, sc, newColor)
        if sc > 0 and image[sr][sc-1] == oldColor: self.floodFill(image, sr, sc-1, newColor)
        if sr < len(image) and image[sr+1][sc] == oldColor: self.floodFill(image, sr+1, sc, newColor)
        if sc < len(image[0]) and image[sr][sc+1] == oldColor: self.floodFill(image, sr, sc+1, newColor)
        
        return image 	