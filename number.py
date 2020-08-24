"""NUMBER RELATED ALGORITHMS"""

"""RANDOM PRIME GENERATOR (RPN)

PRIME NUMBER THEOREM
Define the prime-counting function pi(n) as the number of prime numbers less 
than or equal to some real number n, i.e.
pi(n) = #primes <= n

The prime number theorem states that when n tends to infinity, 
π(n) ≈ n / ln(n).

FERMAT LITTLE THEOREM
If p is a prime number, then for any integer a, the number a**p − a is an 
integer multiple of p, expressed in modular arithmetic as

a**p = a (mod p)

or equivalently a**(p−1) − 1 is an integer multiple of p, or symbolically

a**(p-1) = 1 (mod p)

FERMAT PRIMALITY TEST 
Given n, if there exists a value of a for which a**(n-1) != 1 (mod n), then 
n is composite. Such value for a is called a Fermat witness. If n satisfies 
Fermat’s little theorem for base a, and appears to be prime, then n is 
pseudo-prime of base a.

CARMICHAEL NUMBERS (Ferman liars)
There are some composite numbers that satisfies the Fermat’s little theorem 
for all possible values of a, which are called Carmichael numbers. 

Miller (1976) Riemann's Hypothesis and Tests for Primality
Rabin (1980) "Probabilistic algorithm for testing primality
"""

from random import randrange, getrandbits
from math import sqrt

def isprime(n):
	"""Returns True if the input is a prime number.
	A prime number is 
	- a whole number 
	- greater than 1 
	- only vidisibl3e by one and itself
	Below implements Trial Division of Fibonacci (1202)
	"""
	if n <= 1 or not isinstance(n, int): return False 
	if n == 2: return True
	if n % 2 == 0: return False 
	for i in range(3, int(sqrt(n)-1)//1+2, 2):
		if n % i == 0: return False
	return True 


def primes(n, method="eratosthenes"):
	"""Return all prime numbers upto a given number (inclusive)"""
	if method.lower() == "eratosthenes":
		return _eratosthenes(n)
	elif method.lower() == "sundaram":
		return _sundaram((n-1)//2)

def _eratosthenes(n):
	"""Sieve of Eratosthenes
	
	An array of bits hi is used to mark primality, i.e. 
	mark[i] is True if i+1 is prime
	Eratosthenes -- ancient Greek mathematician
	"""
	prime = [False] + [True] * (n-1)
	k = 2
	while k * k <= n:
		if prime[k-1]:
			for i in range(k*k, n+1, k):
				prime[i-1] = False 
		k += 1
	return [i+1 for i, p in enumerate(prime) if p]

def _sundaram(n):
	"""Sieve of Sundaram

	Start with a list of the integers from 1 to n. 
	From this list, remove all numbers of the form i + j + 2*i*j, where:
	1) 1 <= i <= j
	2) i + j + 2*i*j <= n
	The remaining numbers are doubled and incremented by one, giving a list 
	of the odd prime numbers (i.e., all primes except 2)
	"""
	mark = [True] * n
	for i in range(1, n//3+1):
		for j in range(1, (n-i)//(2*i+1)+1):
			mark[i+j+2*i*j - 1] = False 
	return [2] + [2*(i+1)+1 for i, flag in enumerate(mark) if flag]


class MillerRabin:
	"""Miller-Rabin random prime generator"""
	def __init__(self, bits):
		self.bits = bits

	def isprime(self, n, k=128):
	    """Miller-Rabin primality test
	    The goal of Miller-Rabin is to find a nontrivial square roots of 1 modulo n.
	Take back the Fermat’s little theorem: a**(n-1) = 1 (mod n).
	For Miller-Rabin, we need to find r and s 
	     Test if a number is prime
	        Args:
	            n -- int -- the number to test
	            k -- int -- the number of tests to do
	        return True if n is prime
	    """
	    # Test if n is not even.
	    # But care, 2 is prime !
	    if n == 2 or n == 3: return True
	    if n <= 1 or n % 2 == 0: return False
	    # find r and s such that (n-1) = r*(2**s) where r is odd
	    s, r = 0, n - 1
	    while r & 1 == 0:
	        s += 1
	        r //= 2
		#if ∀ j ∈ [0, s-1],  a**r != 1 (mod n) and a**((2**j)*r) != -1 (mod n), 
		#then n is not prime and a is called a strong witness to compositeness for n.
		#if ∃ j ∈ [0, s-1], a**r = 1 (mod n) or a**((2**j)*r) = -1 (mod n), 
		#then n is said to be a strong pseudo-prime to the base a, and a is called a strong liar to primality for n.
	    for _ in range(k):
	    	#pick a, an integer in the range of [2, n-1]
	        a = randrange(2, n - 1) 
	        #If a**r != 1 (mod n) and a**((2**j)*r) != -1 (mod n) for all j such that 0 ≤ j ≤ s-1
	        #n is not prime and a is called a strong witness to compositeness for n.
	        x = pow(a, r, n) #a**r % n
	        if x != 1 and x != n - 1:
	            j = 1
	            while j < s and x != n - 1:
	                x = pow(x, 2, n)
	                if x == 1: return False
	                j += 1
	            if x != n - 1: return False
	    return True

	def _candidate(self):
	    """ Generate an odd integer randomly
	        Args:
	            bits -- int -- the bits of the number to generate, in bits
	        return a integer
	    """
	    # generate random bits
	    p = getrandbits(self.bits)
	    # apply a mask to set MSB and LSB to 1
	    p |= (1 << self.bits - 1) | 1
	    return p

	def generate(self):
	    """MILLER-RABIN ALGORITHM 
		* Generate a prime candidate and set the MSB and LSB to 1;
		* Test for primarility with Miller-Rabin test;
		* Start from beginning if the number is not prime.
	    Generate a prime
	        Args:
	            bits -- int -- bits of the prime to generate, in bits
	        return a prime
	    """
	    p = 4 #start with smallest non-prime
	    # keep generating while the primality test fail
	    while not self.isprime(p, 128):
	        p = self._candidate()
	    return p


def randprime(bits):
	"""Return a randon prime number of given bits"""
	rpg = MillerRabin(bits) #random prime generator
	n = rpg.generate()
	if not isprime(n):
		n = rpg.generate()
	return n 


if __name__ == "__main__":
	primes = _eratosthenes(100)
	print(primes)
	print(len(primes))