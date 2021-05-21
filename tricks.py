
	"""Interval median distance of array can be calculated in 
	O(N^2) time as below."""
    mdist = [[0]*n for _ in range(n)] # mdist[i][j] median distance of houses[i:j+1]
    for i in range(n):
        for j in range(i+1, n): 
            mdist[i][j] = mdist[i][j-1] + houses[j] - houses[i+j >> 1]