"""SUBSTRING SEARCH
In computer science, string-searching algorithms belogn to a class of string 
algorithms which find the position of a pattern within a text.

                                     operation count 
         algorithm | version     | guarantee | typical | backup? | correct? | space
-----------------------------------------------------------------------------------
       brute force | -           | M*N       | 1.1*N   | yes     | yes      | 1
Knuth-Morris-Pratt | full DFA    | 2*N       | 1.1*N   | no      | yes      | M*R
       mismatch transitions only | 3*N       | 1.1*N   | no      | yes      | M
       Boyer-Moore | full        | 3*N       | N/M     | yes     | yes      | R
  mismatched char heuristic only | M*N       | N/M     | yes     | yes      | R
        Rabin-Karp | Monte Carlo | 7*N       | 7*N     | no      | probable | 1
                   | Las Vegas   | 7*N       | 7*N     | yes     | yes      | 1
-----------------------------------------------------------------------------------

References:
Knuth, Morris & Pratt (1977) Fast pattern matching in strings
Boyer & Moore (1977) A fast string searching algorithm
Karp & Rabin (1987) Efficient randomized pattern-matching algorithms               
"""
from abc import ABC, abstractmethod 

import sys
sys.path.append("C:\\Users\\gaosa\\Documents\\Coding\\algorithms") #make algorithms package visible

from number import randprime
from strings.sort import RADIX 

NOT_FOUND = -1

class StringSearch(ABC):
	"""Abstract base class for string search"""
	def __init__(self, pattern):
		super(StringSearch, self).__init__()
		self.pattern = pattern

	@abstractmethod
	def search(self, text):
		"""Return starting index if pattern is found within text
		otherwise return -1"""
		pass
						

class BruteForce(StringSearch):
	"""Brute-force algorithm for string search
	Check for pattern starting at each text position
	Caveat: 
	1) brute-force algorithm can be slow if text and pattern are repetitive.
	0 1 2 3 4 5 6 7 8 9
	A A A A A A A A A B
	A A A A B
	  A A A A B
	    A A A A B
	      A A A A B
	        A A A A B
	          A A A A B
	2) brute-force algorithm needs "backup" for every mismatch
	"""

	def search(self, text):
		"""
		i points to beginning of sequence of already-matched chars in text 
		j stores # of already-matched chars (end of sequence in pattern)
		"""
		m, n = len(self.pattern), len(text)
		for i in range(n-m+1): #implicit backup
			for j in range(m):
				if text[i+j] != self.pattern[j]: break
			if j == m-1 and text[i+j] == self.pattern[j]: 
				return i #where pattern starts
		return NOT_FOUND

	def search_alt(self, text):
		"""alternative implementation
		i points to end of sequence of already-matched chars in text
		j stores # of already-matched chars (end of sequence in pattern)
		"""
		m, n = len(self.pattern), len(text)
		i = j = 0
		while i < n and j < m:
			if text[i] == self.pattern[j]: 
				j += 1
			else: 
				i -= j #explicit backup
				j = 0
			i += 1
		if j == m: return i - m #found
		else: return NOT_FOUND #not found


class KMP(StringSearch):
	"""Knuth-Morris-Pratt algorithm for string search
	KMP substring search accesses no more than M + N chars to search for a 
	pattern of length M in a text of length N

	Reference: Knuth, Morris & Pratt (1977) Fast pattern matching in strings
	"""
	def __init__(self, pattern):
		super(KMP, self).__init__(pattern)
		self._compute_dfa()

	def _compute_dfa(self):
		"""Compute the deterministic finite-state automation (DFA)
		
		DFA is an abstract string-search machine represented by an RxM matrix
		where R is radix and M equals to length of pattern. Here, state 
		indicates the number of characters in the pattern that have been 
		matched. Utilizing DFA, KMP algorithm can void backup. 

		dfa[c][j] gives the next state of a pattern with first j characters 
		matched when next character is c. 

		               0 1 2 3 4 5
		pattern[j]   | A B A B A C
		             -------------
		  dfa[][j] A | 1 1 3 1 5 1
		           B | 0 2 0 4 0 4
		           C | 0 0 0 0 0 6

		* finite number of states (including start and halt)
		* exactly one transition for each char in alphabet
		* accept if sequence of transitions leads to halt state 
		
		   match transition: in state j & next char pattern[j], go to j+1;
		mismatch transition: back up if c != pattern[j]
		"""
		m = len(self.pattern)
		self._dfa = [[0] * m for _ in range(RADIX)] #RADIX x m matrix
		self._dfa[ord(self.pattern[0])][0] = 1

		x = 0
		for j in range(1, m):
			for c in range(RADIX):
				self._dfa[c][j] = self._dfa[c][x]    #mismatch transition
			self._dfa[ord(self.pattern[j])][j] = j+1 #   match transition
			#key step -- update restart state
			x = self._dfa[ord(self.pattern[j])][x]   

	def search(self, text):
		"""Return starting index if pattern is found within text
		otherwise return -1"""
		m, n = len(self.pattern), len(text)
		i = j = 0
		while i < n and j < m:
			j = self._dfa[ord(text[i])][j] #no backup
			i += 1
		if j == m: return i - m 
		else: return NOT_FOUND


class BoyerMoore(StringSearch):
	"""Boyer-Moore algorithm for string search
	
	mismatched character heuristic:
	* scan characters in pattern from right to left
	* can skip as many as M chars when finding one not in the pattern

 i  j  0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 
------------------------------------------------------------------------------
       F  I  N  D  I  N  A  H  A  Y  S  T  A  C  K  N  E  E  D  L  E  I  N  A 
 0  5  N  E  E  D  L  E <- pattern 
 5  5                 N  E  E  D  L  E 
 11 4                                   N  E  E  D  L  E
 15 0                                               N  E  E  D  L  E

	case 1 -- mismatch character not in pattern 
	case 2 -- mismatch character in pattern 

	Substring search with Boyer-Moore mismatched character heuristic takes 
	about ~N/M character compares to search for a pattern of length M in a 
	text of length N. 

	Caveat: worse-case ~ M*N
	i skip  0 1 2 3 4 5 6 7 8 9 
	        B B B B B B B B B B
	0 0     A B B B B <- pattern
	1 1       A B B B B
	2 1         A B B B B
	3 1           A B B B B
	4 1             A B B B B
	5 1               A B B B B
	"""
	def __init__(self, pattern):
		super(BoyerMoore, self).__init__(pattern)
		self._compute_skiptable()		
		
	def _compute_skiptable(self):
		"""Return the "skip table" (aka right most occurrence) of a character
		in pattern precompute index of rightmost occurrence of character c in 
		pattern (-1 if character not in pattern).

		          SKIP TABLE
		----------------------------------          
		        N  E  E  D  L  E
		c       0  1  2  3  4  5  right[c]
		----------------------------------
		A   -1 -1 -1 -1 -1 -1 -1        -1
		B   -1 -1 -1 -1 -1 -1 -1        -1
		C   -1 -1 -1 -1 -1 -1 -1        -1 
		D   -1 -1 -1 -1  3  3  3         3
		E   -1 -1  1  2  2  2  5         5
		...
		L   -1 -1 -1 -1 -1  4  4         4
		M   -1 -1 -1 -1 -1 -1 -1        -1
		N   -1  0  0  0  0  0  0         0
		...
		"""		
		self.right = [-1] * RADIX
		for j in range(len(self.pattern)):
			self.right[ord(self.pattern[j])] = j

	def search(self, text):
		"""Return starting index if pattern is found within text
		otherwise return -1"""
		m, n = len(self.pattern), len(text)
		i = 0 
		while i <= n-m:
			skip = 0
			for j in reversed(range(m)):
				if self.pattern[j] != text[i+j]:
					#compute skip value 
					skip = max(1, j - self.right[ord(text[i+j])])
					break
			if skip == 0: return i #match
			i += skip 
		return NOT_FOUND 


class RabinKarp(StringSearch):
	"""Rabin-Karp algorithm for string search 

	Monte-Carlo version
	* always runs in linear time
	* extremely likely to return correct answer (but not always!)

	Las Vegas version
	* always return correct answer
	* extremely likely to run in linear time (but worst case is MN)
	"""
	def __init__(self, pattern):
		"""Theory -- IF Q is a sufficiently large random prime (about M*N**2) then the probability of a false collision is about 1/N
		Practice -- Choose to be a large prime (but not so large to cause overflow). Under reasonable assumptions, probability of a collision is about 1/Q"""
		super(RabinKarp, self).__init__(pattern)
		self.Q = randprime(16) #a large prime (but avoid overflow)
		self._compute_pathash()
				
	def _hash(self, string, m):
		"""Return modular hash for m-digit key by using Horner's method to 
		evaluate degree-m polynomial 
		"""
		h = 0
		for j in range(m):
			h = (RADIX * h + ord(string[j])) % self.Q
		return h 

	def _compute_pathash(self):
		"""Compute & store pattern hash"""
		m = len(self.pattern)
		#precompute & store R**(m-1) (mod Q)
		self._rm = 1 
		for _ in range(1, m):
			self._rm = (RADIX * self._rm) % self.Q
		self.pat_hash = self._hash(self.pattern, m)

	def search(self, text):
		"""Return starting index if pattern is found within text
		otherwise return -1 

		Rabin-Karp fingerprint search using modular hashing (Monte Carlo version)
		* compute a hash of pattern characters 0 to m-1
		* for each i, compute a hash of text characters i to i+m-1
		* if pattern hash = text substring hash, check for a match

		x[i] = t[i]*R**(m-1) + t[i+1]*R**(m-2) + ... + t[i+m-1] (mod Q)
		x[i+1] = (x[i] - t[i] * R**(M-1)) * R + t[i+m]

		i   0  1  2  3  4
		-----------------
		    2  6  5  3  5  % 997 = 613

		i   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15
		--------------------------------------------------
		    3  1  4  1  5  9  2  6  5  3  5  8  9  7  9  3
		0   3  1  4  1  5  % 997 = 508
		1      1  4  1  5  9  % 997 = 201
		2         4  1  5  9  2  % 997 = 715
		3            1  5  9  2  6  % 997 = 971
		4               5  9  2  6  5  % 997 = 442
		5                  9  2  6  5  3  % 997 = 929
		6 <- return i=6       2  6  5  3  5  % 997 = 613 <- match
		"""
		m, n = len(self.pattern), len(text)
		txt_hash = self._hash(text, m)
		if self.pat_hash == txt_hash: return 0
		for i in range(m, n):
			txt_hash = (txt_hash + self.Q - self._rm * ord(text[i-m]) % self.Q) % self.Q
			txt_hash = (txt_hash * RADIX + ord(text[i])) % self.Q
			if self.pat_hash == txt_hash: return i - m + 1 #Monte-Carlo version
		return NOT_FOUND 


if __name__ == "__main__":
	text = "ABCCBAAAB"
	pattern = "AAB"
	print(KMP(pattern).search(text))
	print(BoyerMoore(pattern).search(text))
	print(RabinKarp(pattern).search(text))