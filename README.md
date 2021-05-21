Below is a summary of APIs and their implementations & locations. 

API            | implementation  | library
---------------------------------------------
bag            | array           | containers
bag            | linked list     | linkedlist
graph          | adjancency list | graph
priority queue | heap            | tree
queue          | array           | containers
queue          | linked list     | linkedlist
quick find     | array           | containers
quick union    | tree            | containers
stack          | array           | containers
stack          | linked list     | linkedlist
symbol table   | bs tree         | tree

web crawler
goal - crawl web, starting from some root web page, say google.com. 

BFS with implicit digraph
* choose root web page as source s;
* maintain a queue of websites to explore;
* maintain a set of discovered websites;
* dequeue the next website and enqueue websites to which it links


Bird's-eye view (complexity zoo)
complexity | order of growth | examples
-------------------------------------------------------------------------------------
linear     | N               | min, max, median, Burrows-Wheeler transform, ...
linearithmic | N * log(N)    | sorting, convex hull, closest pair, farthest pair, ...
quadratic  | N**2            | ?
...        | ...             | ...
exponential | exp(N)         | ?

Frustrating news -- huge number of problems have defied classification

Reduction
Problem X reduces to problem Y if you can use an algorithm hat solves Y to help solve X. 
cost of solving X = cost of solving Y + cost of reduction (preprocessing & postprocessing)

Lower Bound
Linear-time reduction
Def. Problem X linear-time reduces to problem Y if X can be solved with
* linear number of standard computational steps
* constant number of calls to Y

INDEX 
Kruskal's algorithm | Joseph Kruskal | | minimal spanning tree
   Prim's algorithm | Robert Prim    | | minimal spanning tree
Huffman's algorithm | David Huffman  | 1952 | compression
Rabin-Karp algorithm | Michael Rabin, Dick Karp | 
Brewer's problem | 


complexity of integer multiplication history
year | alglrithm          | order of growth
------------------------------------------------
?    | brute-force        | N**2
1962 | Karatsuba-Ofman    | N**1.585 <- divide & conquer
1963 | Toom-3, Toom-4     | N**1.465, N**1.404
1966 | Toom-Cook          | N**(1+epsilon)
1971 | Schonhage-Strassen | N*log(N)*log(log(N))
2007 | Furer              | N*log(N)*2**(log(N))

TOP 10 SCIENTIFIC ALGORITHMS OF 20TH CENTURY
1
2
3
4
5
6
7
8
9
10

A problem is "intractable" if it cannot be solved in polynomial time.

A universal model of computation -- Turing machine
Q: Is there a more powerful model of computation?
A: No! <- most important scientific result of 20th century? 
Turing machines can compute any functions that can be computed by a physically harnessable process of the natural world

Stirling's approximation
ln(n!) = nln(n) - n + O(ln(n))
n! ~ sqrt(2pi*n)(n/e)**n

Four fundamental problems
LSOLVE. Given a system of linear equations, find a solution.
LP    . Given a system of linear inequalities, find a solution.
ILP   . Given a system of linear inequalities, find a binary solution. 
SAT   . Given a system of boolean equations, find a binary solution. 

Q: Which of these problems have poly-time algorithms?
LSOLVE. Yes. Gaussian elimination solves N-by-N system in N**3 time
LP    . Yes. Ellipsoid algorithm is poly-time 
ILP, SAT. No poly-time algorithm known or believed to exist

SEARCH PROBLEMS
OPTIMIZATION PROBLEMS

Def. NP is the class of all search problems 
Def. P is the class of search problems solvable in poly-time. 

NP -- nondeterministic polynomial time
 P --                  polynomial time

P = NP ? Can you always avoid brute-force searching and do better
overwehlming censensus P != NP

Millennium Prize Problems by Clay Mathematics Institute (11/24/2000)
- Birch & Swinnerton-Dyer conjecture
- Hodge conjecture
- Navier-Stokes existence and smoothness
- P vs NP problem
- Poincare conjecture
- Riemann hypothesis
- Yang-Mills existence and mass gap

problem | description | poly-time algo | instance | solution
------------------------------------------------------------
LSOLVE
LP
ILP
SAT
FACTOR 

Exhaustive search
Q: How to solve an instance of SAT with n variables?
A: Exhaustive search -- try all 2**n truth assignments.

Q: Can we do anything substantially more clever?
Conjecture: No poly-time algorithm for SAT (intractable)

Cook reduction: Problem X poly-time reduces to problem Y if X can be solved with
- polynomial number of standard cmputational steps
- polynomial number of calls to Y

SAT reduces to ILP 

NP-compleness (NPC)
Def. An NP problem is NP-complete if all problems in NP poly-time reduce to it. 

Proposition (Cook 1971). SAT is NP-complete (every NP problem is a SAT in disguise)

Corollary. Poly-time algorithm for SAT iff P = NP.
SAT captures difficulty of whole class of NP. 

1926: Ising introduces simpel model for phase transitions
1944: Onsager finds closed form solution to 2D version in tour de force
19xx: Feynman and other top minds seek 3D solution
2000: 3D-ISING proved NP-complete

NP = P + NPC + others

 P -- class of search problems solvable in poly-time
NP -- class of all search problems, some of which seem wickedly hard
NP-complete -- hardest problems in NP
intractable -- problem with no poly-time algorithm 

RSA -- 

FACTOR. Given an n-bit integer x, find a nontrivial factor.
Q: What's complexity of FACTOR?
A: In NP, but not known (or believed) to be in P or NP-complete. 

