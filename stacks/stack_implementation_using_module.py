import collections
import queue

stack_v1 = collections.deque()
stack_v2 = queue.LifoQueue(5) # max elements that stack takes

stack_v1.append(10)
stack_v1.append(20)
stack_v1.append(30)

print(stack_v1.pop())

stack_v2.put(40)
stack_v2.put(50 , timeout=1) # time it takes to print error message and this time out is applicable for both put and get methods in lifoqueue.

print(stack_v2.get())