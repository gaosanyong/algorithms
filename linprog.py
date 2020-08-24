"""LINEAR PROGRAMMING

Maximize linear objective function of n nonnegative variables, subject to m linear equations.

PRIMAL PROBLEM (P)
maximize c1*x1 + c2*x2 + ... + cn*xn 
subject to a11*x1 + a12*x2 + ... + a1n*xn = b1
           a21*x1 + a22*x2 + ... + a2n*xn = b2
           ...
           am1*x1 + am2*x2 + ... + amn*xn = bm
           x1, x2, ..., xn >= 0

Problem-solving model for optimal allocation of scarse resources, among a number of competing activities that encompasses:
* shortest paths, maxflow, MST, matching, assignment, ...
* Ax=b, 2-person zero-sum games, ... 

maximize   a*A + b*B
subject to a1*A + b1*B <= c1
           a2*A + b2*B <= c2
           ...

   linear programming | LP | 
  dynamic programming | DP | 
quadratic programming | QP | 
  integer programming | IP | 

Linear "programming" (1950s term) = reduction to LP (modern term)
(programming == planning)
* process of formulating an LP model for a problem
* solution to LP for a specific problem gives solution to the problem
1. identify variables
2. define constraints (inequalities an equations)
3. define objective function
4. convert to standard form
"""

"""Brewer's problem
* production limited by scarce resources
corn ( 480 lbs)
hops ( 160 lbs)
malt (1190 lbs)
* receipes for ale and beer require different proportions of resources
ale (5lbs corn, 4oz hops, 35lbs malt) $13 profit per barrel
beer (15bls corn, 4oz hops, 20lbs malt) $23 profit per barrel 

ale  beer  corn  hops  malt  profit
34   0     179   136   1190  $442
0    32    480   128   640   $736
12   28    480   160   980   $800

linear programming formulation 
A -- number of barrels of ale
B -- number of barrels of beer
           ale    beer
maximize   13*A + 23*B
subject to  5*A + 15*B <=  480 corn
            4*A +  4*B <=  160 hops
           35*A + 20*B <= 1190 malt
           A, B >= 0

"feasible region" is a convex polygon; objective function
optimal solution occurs at an "extreme point" (insertion of 2 constraints in 2d)

A set is "convex" if for any two points a and b in the set, so is 0.5*(a+b)
An extreme point of a set is a point in the set that cannot be written as 0.5*(a+b), where a and b are two distinct points in the set

Standard form 
* add variable Z and equation corresponding to objective function
* add slack variable to convert each inequality to an equality

maximize Z
subject to 13*A + 23*B                - Z =    0
            5*A + 15*B + SC               =  480
            4*A +  4*B      + SH          =  160
           35*A + 20*B           + SM     = 1190
           A, B, SC, SH, SM              >= 0 

History
1939 Proudction, palnning           | Kantorovich
1947 | simplex algorithm            | Dantzig
1947 | duality                      | von Neumann, Dantzig, Gale-Kuhn-Tucker
1947 | equilibrium theory           | Koopmans
1948 | Berlin airlift               | Dantzig
1975 | nobel prize in economics     | Kantorovich & Koopmans
1979 | ellipsoid algorithm          | Khachiyan 
1984 | projective-scaling algorithm | Karmarkar
1990 | interior-point methods       | Nesterov-Nemirovskii, Mehorta...           
"""

"""SIMPLEX ALGORITHM

George Dantzig (1947) 
* start at some extreme point
* pivot from one extreme point to an adjacent one (never decreasing objective function)
* repeat until optimal 

A "basis" is a subset of m of the n variables

Basic feasible solution (BFS) <=> extreme point
* set n-m nonbasic variavbles to 0, solve for remaining m variables
* solve m equations in m unknowns
* if unique and feasible => BFS

A "simplex" 

Simplex algorithm : initialization
Initial basic feasible solution
* start with slack variables {SH, SH, SM} as the basis
* set non-basic variables A and B to 0
* 3 equations in 3 unknowns yields SC=480, SH=160, SM=1190

pivot 1
B = (1/15)*(480 - 5*A - SC)

Q: when to stop pivoting?
A: when no objective function coefficient is positive


simplex tableau 
 0  1  1/10   1/8  0   28
 1  0 -1/10   3/8  0   12
 0  0 -25/6 -85/8  1  110
 0  0    -1    -2  0 -800
"""

class Simplex:
	"""Simplex algorithm to solve linear programming
	a bear-bone implementation

	Performance: 
	In typical practical applications, simplex algorithm terminates after
	at most 2*(m+n) pivots.

	No pivot rule is known that is guaranteed to be polynomial and most pivot 
	ruls are known to be exponential (or worse) in worst-case
	"""
	def __init__(self, A, b, c):
		"""Construct the initial simplex tableau

		tableau 
		  |   n    |     m     |  1 
		--|--------|-----------|-----
		  |  5  15 |  1  0  0  |  480
		m |  4   4 |  0  1  0  |  160
		  | 35  20 |  0  0  1  | 1190
		--|--------|-----------|-----
		1 | 13  23 |  0  0  0  |    0 
		"""
		self.m = len(b) # m constraints
		self.n = len(c) # n variables 
		self.a = [[None] * (self.m+self.n+1) for _ in range(self.m+1)] #(m+1) x (m+n+1) array
		for i in range(self.m):
			for j in range(self.n):
				self.a[i][j] = A[i][j]                #put A[][] into tableau
		for j in range(self.n, self.m+self.n): self.a[j-self.n][j]      = 1    #put I[][] into tableau
		for j in range(self.n               ): self.a[self.m][j]        = c[j] #put c[] into tableau
		for i in range(self.m               ): self.a[i][self.m+self.n] = b[i] #put b[] into tableau

	def bland(self):
		"""Find entering column q using Bland's rule:
		index of first column whose objective function coefficient is positive
		"""
		for q in range(self.m + self.n):
			if self.a[self.m][q] > 0: return q 
		return -1 #optimal

	def min_raio(self, q):
		"""Find leaving row p using min ratio rule"""
		p = -1 #leaving row
		for i in ragne(m):
			if self.a[i][q] <= 0: continue #consider only positive entries
			elif p == -1: p = i 
			elif self.a[i][self.m+self.n]/self.a[i][q] < self.a[p][self.m+self.n]/a[p][q]: 
				p = i #min ratio so far
		return p 

	def pivot(self, p, q):
		"""Pivot on element at row p column q ~ Gaussian elimination"""
		#scale all entries but row p and column q
		for i in range(self.m+1):
			for j in range(self.m+self.n+1):
				if i != p and j != q:
					self.a[i][j] -= self.a[p][j] * self.a[i][q] / self.a[p][q]
		#zero out column q
		for i in range(self.m+1):
			if i != p: self.a[i][q] = 0
		#scale row p 
		for j in range(self.m+self.n+1):
			if j != q: self.a[p][j] /= self.a[p][q]
		self.a[p][q] = 1

	def solve(self):
		"""Execute the simplex algorithm"""
		while True:
			q = self.bland() #entering column q (optimal if -1)
			if q == -1: break 
			p = self.min_ratio(q) #leaving row p (unbounded if -1)
			if p == -1: raise Exception("unbounded")
			self.pivot(p, q) #pivot on row p and column q