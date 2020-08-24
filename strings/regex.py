"""REGULAR EXPRESSION

   |------------------------------------------|
   | RE --(parse)--> NFA --(simulate)--> text |
   |------------------------------------------|

A regular expression is a notation to specify a set of strings. 

operation     | order | example RE | matches       | does not match 
-----------------------------------------------------------------------
concatenation | 3     | AABAAB     | AABAAB        | every other string
or            | 4     | AA|BAAB    | AA BAAB       | every other string
closure       | 2     | AB*A       | AA ABBBBBBBBA | AB ABABA
parentheses   | 1     | (AB)*A     | ABABABABABA   | ABBA

Additional operations are often added for convenience

wildcard      | .U.U.U. | CUMULUS | SUCCUBUS
char class    | [A-Za-z][a-z]* | word capitalized | camelCase 
at least 1    | A(BC)+DE | ABCDE | ADE
exactly k     | [0-9]{5}-[0-9]{4} | 08540-1321 | 111111111

[A-E]+ is shorthand for (A|B|C|D|E)(A|B|C|D|E)*

substring search | .*SPB.* 
social security numbers [0-9]{3}-[0-9]{2}-[0-9]{4}
email address | [a-z]+@([a-z]+\.)+(edu|com) 
Java identifier | [$_A-Za-z][$_A-Za-z0-9]* 

REs play a well-understood role in the theory of computation. 

Writing a RE is like writing a program
- need to understand programming model
- can be easilier to write than read
- can be difficult to debug

Bottom line -- REs are amazingly powerful and expressive, but using them in applications can be amazingly complex and error-prone. 

Duality between REs and DFAS
DFA -- deterministic finite-state atomata, state machine to recognize whether a given string is in a given set

Kleene's theorem
* for any DFA, there exists a RE that describes the same set of strings
* for any RE, there exists a DFA that recognizes the same set of strings

NFA -- nondeterministic finite-state automata
Basic plan (apply Kleene's theorem)
- build NFA from RE
- simulate NFA with text as input

regex-matching NFA
- RE enclosed in parentheses
- one state per RE character (start = 0, accpet = M)
- red epsilon-transition (change state, but doesn't scan text)
- black match transition (change state and scan to next char)
- accept if any sequence of transitions ends in accept state 

NFA representation
- state names: integers from 0 to M;
- match transition: keep regex in array re[];
- epsilon transition: store in a digraph. 

NFA simulation
Q: how to efficiently simulate an NFA?
A: maintain set of all possible states that NFA could be in after reading in the first i text characters

Q: how to perform reachability? 

digraph reachability -- find all vertices reachable from a given source or set of vertices

solution: run DFS from each source, without unmarking vertices
performance: ~ E + V

"""

class DirectedDFS:
	"""Find vertices reachable from given state"""
	def __init__(self, graph, state):
		self.graph = graph
		self.state = state

	def marked(self, vertex):
		pass
		

class NFA:
	"""Nondeterministic finite-state automata
	
	Determining whether an N-character text is recognized by the NFA 
	corresponding to an M-character pattern takes time proportional to 
	M*N in the worst case. (For each character in the text, we need to 
	perform a graph reachability computation on a digraph with M vertices 
	and at most 3*M edges). 
	"""
	def __init__(self, regexp):
		""""""
		self.m = len(regexp) #number of states 
		self.re = list(regexp) #match transitions
		self.graph = build_epsilon_transition_digraph() #epsilon transition digraph

	def recognize(self, text):
		""""""
		pc = Bag()
		dfs = DirectedDFS(self.graph, 0) #state reachable from start by epsilon-transition
		for v in self.graph:
			if dfs.marked(v): pc.add(v) 

		for i in range(len(text)):
			match = Bag() #state reachable after scaning past text[i]
			for v in pc:
				if v == m: continue
				if self.re[v] == text[i] or self.re[v] == ".":
					match.add(v+1) 
			dfs = DirectedDFS(self.graph, match)
			pc = Bag()
			for v in self.graph:
				if dfs.marked(v): pc.add(v)

		for v in pc:
			if v == m: return True
		return False 

	def build_epsilon_transition_digraph(self):
		"""Build the NFA corresponding to an m-character RE

		time ~ O(m) & space ~ O(m)
		"""
		digraph = Digraph(self.m+1)
		ops = Stack()
		for i in range(m):
			lp = i 
			if self.re[i] == "(" or re[i] == "|": ops.push(i) #left parenthese and |
			elif self.re[i] == ")":
				or_ = ops.pop()
				if self.re[or_] == "|": #or
					lp = ops.pop()
					digraph.add_edge(lp, or_+1)
					digraph.add_edge(or_, i)
				else:
					lp = or_
			#closure (need 1-character lookahead)
			if i < self.m - 1 and self.re[i+1] == "*": 
				digraph.add_edge(lp, i+1)
				digraph.add_edge(i+1, lp)
			#metasymbols
			if self.re[i] == "(" or self.re[i] == "*" or self.re[i] == ")":
				digraph.add_edge(i, i+1)
		return digraph 

		
"""Building an NFA corresponding to an RE
concatenation | add match-transition edge from state corresponding to characters in the alphabet to next state 
parentheses   | add epsilon-transition edge from parentheses to next state
closure       | add three epsilon-transition edges from each * operator 
or            | add two epsilon-transition edges for each | operator 

maintain a stack
( symbol: push ( onto stack
| symbol: push | onto stack
) symbol: pop corresponding (and possibly intervening |; add epsilon-transitionedges for closure/or
"""

import sys

class GREP:
	"""Ken Thompson's grep
	Generalized regular expression print"""
	def __init__(self, pattern):
		self.pattern = pattern
		regexp = "(.*" + pattern + ".*)"
		nfa = NFA(regexp)
		for line in sys.stdin:
			if nfa.recognize(line):
				print(line)

"""NOT-SO-REGULAR EXPRESSION

back-references
- \1 notation matches subexpression that was matched earlier 
- supported by typical RE implementations
pattern matching with back-references is intractable

"""				