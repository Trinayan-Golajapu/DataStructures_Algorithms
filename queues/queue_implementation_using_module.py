import collections

queue = collections.deque()

queue.appendleft(10)
queue.appendleft(20)
queue.appendleft(30)

print(queue.pop())

# we can use append and popleft combination as well.

# --------------------------------------------------------------------------------

import queue

q = queue.Queue() # maxsize = number of items

q.put_nowait(10) # put method is also there with same functionality
q.put_nowait(20)

print(q.get_nowait()) # get method is also there with same functionality

# --------------------------------------------------------------------------------

pq = queue.PriorityQueue()

pq.put(100)
pq.put(2)
pq.put(34)
pq.put(45)

print(pq.get())