# brute force

from collections import deque
nums = [1,3,-1,-3,5,3,6,7]
k = 3

q = deque()

res = []

for i in nums:
    
    q.append(i)
    
    if len(q) == k:
        res.append(max(q))
        q.popleft()

print(res)

