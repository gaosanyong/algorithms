# inputs
times = [10, -4, 6, 6, 3 ] # a list of times
time_ints = [(1, 6), (6, 6), (0, 2), (10, 15)] # a list of time intervals 
# outputs
answer = {-4: [], 3: [(1, 6)], 6: [(1, 6), (6, 6)], 10: [(10, 15)]}

#benchmark
ans0 = dict()
step = 0
for time in times:
    temp = []
    for time_int in time_ints:
        step += 1
        if time_int[0] <= time <= time_int[1]: temp.append(time_int)
    ans0[time] = temp
print(step)
print(ans)

#improvement 
times.sort()
time_ints.sort() 

ans = dict()
step = j = 0
for time in times:
    intervals = []
    i = j
    while i < len(time_ints):
        step += 1
        start, end = time_ints[i]
        if time < start: break 
        elif start <= time <= end: intervals.append(time_ints[i])
        else: j = i + 1
        i += 1
    ans[time] = intervals
print(step)
print(ans)
print(ans0 == ans)