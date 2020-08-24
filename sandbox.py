import time

#memoized solition II
def fib(n, memo=dict()):
    if n in memo: return memo[n]
    if n == 0 or n == 1: return n
    memo[n] = fib(n-1, memo) + fib(n-2)
    return memo[n]

def flatten(nested):
	ans = []
	for x in nested:
		if isinstance(x, list): 
			ans.extend(flatten(x))
		else: 
			ans.append(x)
	return ans 


# import threading

# def fn():
# 	nonlocal lock
# 	lock.acquire() #
# 	pass
# 	lock.release() 

# lock = threading.Lock()


if __name__ == "__main__":
	# start = time.time()
	# print(fib(5))
	# finish = time.time()
	# print(f"Finished in {finish-start} secs")

	nested = [1, [2, [3, [4, [], 5], 6], 7], 8]
	flattened = flatten(nested)
	print(flattened)