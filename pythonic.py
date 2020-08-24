"""
#MAXIMUM NUMBERS 
MAXPOS = float("inf")  #only floating
MAXNEG = float("-inf") #only floating

#REVERSE
a = a[::-1]

#INITIALIZATION
a = b = 0
a, b = 0, 1
(a, b) == (0, 1)

#COMPARISON
a == b == c
a <= b <= c

#SWAP
a, b = b, a

#ROUND UP/DOWN 
a = n//d #round down 
a = (n-1)//d + 1 #round up (d != 1)

a = (n - 0.5)//1 + 1 #round to nearest integer
a = n//1             #round down to nearest integer
a = (n - )


#LOOP THROUGH NUMBERS WITH N DIGITS 
for i in range(10**(n-1) - (n==1), 10**n):
	pass 

#DICTIONARY OF LISTS
l = [5, 7, 7, 8, 4, 3, 3, 2]
d = {}
for i, v in enumerate(l):
	d.setdefault(v, []).append(i)

#SORTED INDICES
l = [5,4,3,2,1]
sorted(range(len(l)), key=lambda i: a[i])
sorted(enumerate(l), key=lambda x: x[1])

#POLYNOMIAL f(x) = ((((a5 * x + a4) * x + a3) * x + a2) * x + a1) * x + a0
#Horner's method
from functools import reduce
coef = [a5, a4, a3, a2, a1, a0]
poly = lambda x: reduce(lambda a, b: a * x + y, coef)

#FILTERING NONE
result = filter(None, [1,2,3,4,5,None]) #result is a generator

#CUMULATIVE SUM/SUM/MIN
def cumsum(nums):
	sum_ = 0
	for num in nums: 
		sum_ += num
		yield sum_

from itertools import accumulate
accumulate(nums)

#SLIDING WINDOW SUM
window = [sum(a[i:i+k]) for i in range(len(a)-k)] #O(k)

num = 0
for i in range(len(a)):
	num += a[i]
	if i >= k-1: 
		#do something
		num -= a[i-(k-1)]

max_ = float("-inf")
for num in nums: max_ = max(max_, num)

min_ = float("inf")
for num in nums: min_ = min(min_, num)

import operator
index, value = max(enumerate(list_), key=operator.itemgetter(1))

max(l)                                 #max value
max(range(len(l)), key=lambda i: a[i]) #index of max value
max(enumerate(l), key=lambda x: x[1])  #index-value pair of max value

#ALL SAME 
len(set(list_)) == 1

#LIST INDEXING & SLICING
array[i]
array[-i]
array[~i] #same as array[-i-1]
array[i:]
array[:i]


#find all occurrence of a substring
#method 1 -- regular expression
import re
found = [m.start() for m in re.finditer(pattern, text)]

#method 2 -- built-in find method
start = -1
found = []
while True:
	start = text.find(pattern, start+1)
	if start == -1: break 
	found.append(start)

#TRIE
from collections import defaultdict
Trie = lambda: defaultdict(Trie)
trie = Trie()
END = True
reduce(trie.__getitem__, word, trie)[END] = ...

#COUNT SET BIT
bin(num).count("1")

#MATRIX
ZEROS = [[0]*n for _ in range(m)] #zero matrix
ONES  = [[1]*n for _ in range(m)] #one matrix
RANDOM = [[random() for _ in range(n)] for _ in range(m)] #random matrix

for row in matrix:
	for val in row: 
		pass

for i in range(m):
	for j in range(n):
		matrix[i][j] #impossible to break 

from itertools import product
for i, j in product(range(m), range(n)):
	matrix[i][j] #possible to break 

#MATRIX TRANSPOSE
zip(*matrix)

#FLATTEN matrix (NESTED LIST) into array
nested = [[1,2,3], [4,5,6]]
flattened = [x for l in nested for x in l] #comprehension
flattened = sum(nested, []) #sum built-in function (slow)

#CONVERT array into matrix
flattened = [1,2,3,4,5,6]
nested = [flattened[i:i+3] for i in range(0, len(flattened), 3)] #2x3 matrix

#NEIGHBOR of point i, j
(i-1, j-1)  (i-1, j)  (i-1, j+1)
(i  , j-1)  (i  , j)  (i  , j+1)
(i+1, j-1)  (i+1, j)  (i+1, j+1)

neighbors = ((-1,-1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1))
neighbors = product((-1,0,1), (-1,0,1))

def neighbors(i, j):
	for ii, jj in product(range(i-1,i+2), range(j-1,j+2)):
		yield ii, jj 

neighbors = ((-1,0), (1,0), (0,-1), (0,1))
def neighbors(i, j):
	for ii, jj in ((i-1,j), (i+1,j), (i,j-1), (i,j+1)):
		if 0 <= ii < m and 0 <= jj < n: 
			yield ii, jj 

from itertools import product
neighbor = product([-1, 0, 1], [-1, 0, 1])

#COPY A MATRIX
copy = [[matrix[i][j] for j in range(n)] for i in range(m)]

from copy import deepcopy
copy = deepcopy(matrix) #DEEP COPY A MATRIX

#CHECK VALUE IN MATRIX
exist = any(value in row for row in matrix)


from functools import reduce
number = reduce(lambda x, y: 10*x + y, digits) #DIGITS TO NUMBER
number = int("".join(map(str, digits)))
digits = [int(x) for x in str(number)] #NUMBER TO DIGITS

#REMOVE PUNCTUATION
from string import punctuation
table = str.maketrans("", "", punctuation)
"hit.".translate(table)

#YIELD FROM
def generator():
	yield from generator1()
	yield from generator2()

#NESTED FUNCTION & CLOSURE 
#1) nested function has access to variables in outer function
#2) nested function cannot change variables in outer function unless (1) mutable or (2) nonlocal

#MEDIAN 
median = (a[(len(a)-1)//2] + a[len(a)//2])/2

#LETTER TO NUMBER MAPPING
mapping = dict(zip(letters, range(len(letters))))
mapping = {c:i for i, c in enumerate(letters)}

#CONVERT NUMBER TO array OF DIGITS
digits = list(map(int, str(number)))
number = int("".join(map(str, digits)))

#LETTER -> FREQUENCY TABLE
from collections import Counter
freq = Counter(word)

freq = defaultdict(int)
for letter in word:
	freq[letter] += 1

freq = dict()
for letter in word:
	freq[letter] = word.count(letter)

ans = []
for k, v in freq.items():
	ans.extend([k]*v)

#NUMBER OF DIGITS OF AN INTEGER
ndigit = len(str(number))

from math import log10 
ndigit = int(log10(number)) + 1

#PRODUCT
product(["abc", "def", "ghi"])

"""