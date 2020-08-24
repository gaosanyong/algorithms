"""DATA COMPRESSION

Lossless compression
Huffman : represent fixed-length symbols with variable-length codes
LZW     : represent variable-length symbols with fixed-length codes

Lossy compression 
* JPEG, MPEG, MP3
* FFT, wavelets, fractals

Theoretical limits on compression -- Shannon entropy
H(x) = -p(x)log(p(x))

most files have lots of redundancy

Moore's law : # transistors on a chip doubles every 18-24 months 

generic file compression
- files: gzip, bzip, 7z
- archives: pkzip
- file systems: NTFS, HFS+, ZFS

message: binary data B we want to compress
compress: generates a "compressed" representation C(B)
expand: reconstructs original bitstream B

bitstream (B) --(compress)--> compressed version C(B) --(expand)--> original bitstream B

compression ratio = bits in C(B) / bits in B
50-75% compression for natural language 

Date representation 
1) string "12/31/1999" - 80bits
2) 3 integers (12, 31, 1999) - 96bits
3) (month, 4), (day, 5), (year, 12) - 21bits

Proposition: NO algorithm can compress every bitstring 

Lossless compression
- remove redundancy 
- improve encoding 

Static model -- same model for all texts
* fast 
* not optimal -- different texts have different statitical properties
* ex -- ASCII, Morse code

Dynamic model -- generate model based on text
* preliminary pass needed to generate model
* must transmit the model
* ex -- Huffman code

Adaptive model -- progressively learn and update model as you read text
* more accurate modeling produces better compression
* decoding must start from beginning
* ex -- LZW 

Lempel-Ziv & friends
* LZ77
* LZ78
* LZW
* Deflate / zlib = LZ77 variant + Huffman

LZW | Unix compress, GIF, TIFF, V.42bis modem
deflate / zlib | zip, 7zip, gzip, jar, png, pdf

Lossless data compression benchmarks
year | scheme          | bits/char
----------------------------------
1967 | ASCII           | 7.00
1950 | Huffman         | 4.70
1977 | LZ77            | 3.94
1984 | LZMW            | 3.32
1987 | LZH             | 3.30
1987 | move-to-front   | 3.24
1987 | LZB             | 3.18 
1987 | gzip            | 2.71
1988 | PPMC            | 2.48
1994 | SAKDC           | 2.47
1994 | PPM             | 2.34
1995 | Burrows-Wheeler | 2.29
1997 | BOA             | 1.99
1999 | RK              | 1.89

"""


"""Run-length encoding


"""

from math import log 
import sys

class RunLength:
	"""Run-length encoding for lossless compression"""
	def __init__(self, R):
		self.R = R #max run-length count
		self.lgR = log2(R) #number of bits per count 

	def compress(self):
		pass

	def expand(self):
		""""""
		bit = False 
		while sys.stdin: 
			run = sys.stdin.read(lgR) #read 8-bit count from standard input
			for i in range(run):
				BinaryStdOut.write(bit) #write 1 bit to standard output
		BinaryStdOut.close()


"""Huffman Compression

David Huffman 

Morse code 
A *-      1 *----
B -***    2 **---
C -*-**   3 ***--
D N-**    4 ****-
E *       5 *****
F **-*    6 -****
G --*     7 --***
H ****    8 ---**
I **      9 ----*
J *---    0 -----
K -*-
L *-**
M --
N -*
O ---
P *--*
Q --*-
R *-*
S ***
T -
U **-
V ***-
W *--
X -**-
Y -*--
Z --**

Ex. ***---***
SOS?
V7?
IAMIE?
EEWNI?

Q: How do we avoid ambiguity?
A: Ensure that no codeword is a prefix of another.

Ex 1. fixed-length code
Ex 2. append special stop char to each codeword
Ex 3. general prefix-free code 

prefix-free code -- trie representation

"""

class HuffmanNode:
	"""Huffman trie node"""
	def __init__(self, char, freq, left=None, right=None):
		"""Initialize a Huffman trie node"""
		self.char = char
		self.freq = freq
		self.left = left
		self.right = right
	
	def isleaf(self):
		"""Return True if node is a leaf"""
		return self.left is None and self.right is None

	#rich comparsion method
	def __eq__(self, other):
		return self.freq == other.freq

	def __ne__(self, other):
		return self.freq != other.freq

	def __lt__(self, other):
		return self.freq < other.freq

	def __le__(self, other):
		return self.freq <= other.freq

	def __gt__(self, other):
		return self.freq > other.freq

	def __ge__(self, other):
		return self.freq >= other.freq


	def expand(self):
		"""	"""
		root = read_trie() #read in encoding trie
		n = BinaryStdIn. #read in number of chars

		for i in range(n):
			x = root
			while not x.islreaf():
			#expand codeword for ith char 
				if not BinaryStdIn.readBoolean():
					x = x.left
				else:
					x = x.right 
			BinaryStdOut.write(x.ch, 8)
		BinaryStdOut.close()


	def write_trie(self, x):
		if x.isleaf():
			BinaryStdOut.write(True)
			BinaryStdOut.write(x.ch, 8)
			return 
		BinaryStdOut.write(False)
		write_trie(x.left)
		write_trie(x.right)

	def read_trie(self):
		""""""
		if BinaryStdIn.readBoolean():
			char = BinaryStdIn.readChar(8)
			return HuffmanNode(char, 0, None, None)
		left = read_trie()
		right = read_trie()
		return HuffmanNode("\0", 0, left, right)

"""Shannon-Fano algorithm
- partition symbols S into two subsets S0 and S1 of (roughly) equal freq
- codewords for symbols in S0 start with 0; for symbols in S1 start with 1;
- recur in S0 and S1
"""

"""Huffman algorithm (find optimal prefix-free code)

* count frequency freq[i] for each char i in input
* start with one node corresponding to each char i (with weight freq[i])
* repeat until single trie formed 
- select two tries with min weight freq[i] and freq[j]
- merge into single trie with weight freq[i] + freq[j]

Huffman algorithm produces an optimal prefix-free code

Huffman (1952) A method for the construction of minimum-redundancy codes 

implementation
pass 1 -- tabulate char frequencies
pass 2 -- encode file by traversing trie or lookup table 

Running time (using a binary heap) ~ N + Rlog(R) 
"""

from tree import MinQueue

def build_trie(freq):
	"""Construct a Huffman encoding trie"""
	pq = MinQueue()
	for i in range(R): #initialize pq with singleton tries
		pq.insert(HuffmanNode(i, freq[i], None, None))

	while pq: #merge two smallest tries 
		x = pq.del_min()
		y = pq.del_min()
		parent = HuffmanNode('\0', x.freq + y.freq, x, y)  #not used for internal nodes
		pq.insert(parent)

	return pq.del_min()


"""Lempel-Ziv-Welch (LZW) algorithm 

  input | A  B  R  A  C  A  D  A  B  R  A  B  R  A  B  R  A
matches | A  B  R  A  C  A  D  AB    RA    BR    ABR      A
  value | 41 42 52 41 43 41 44 81    83    82    88       41


  key | value    key | value    key | value
  A     41       AB    81       DA    87
  B     42       BR    82       ABR   88
  C     43       RA    83       RAB   89
  D     44       AC    84       BRA   8A
                 CA    85       ABRA  8B
                 AD    86
LZW algorithm
* create symbol table associating W-bit codewords with string keys
* initialize symbol table with codewords for single-char keys
* find longest string s in symbol table that is a prefix of unscanned part of input
* write the W-bit codeword associated with s
* add s + c to symbol table, where c is next char in the input 

Q: How to represent LZW compression code table?
A: A trie to support longest prefix match 

LZW expansion
* create symbol table associating string values with W-bit keys
* initialize symbol table contain single-char values
* read a W-bit key
* find associated string value in symbol table and write it out
* update symbol table

Q: How to represent LZW expansion code table?
A: An array of size 2**W
"""

def compress(self):
	input = BinaryStdIn.readString() #read in input as string
	st = TST()
	for i in range(R): #codewords for single char, radix R keys
		st.put("" + str(i), i)
	code = R + 1
	while input:
		s = st.longest_prefix(input) #find longest prefix match s
		BinaryStdOut.write(st.get(s), W) #write W-bit codewords for s
		t = len(s) 
		if t < len(input) and code < L:
			code += 1
			st.put(input[0:t+1], code) #add new codeword
		input = input[t]

	BinaryStdOut.write(R, W) #write "stop" codeword 
	BinaryStdOut.close()     #close input stream 

