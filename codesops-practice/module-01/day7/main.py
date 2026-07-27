stack = [] # last- in frist out 
stack.append(1)  # Stack: [1]
stack.append(2)  # Stack: [1, 2]
top_item = stack.pop()  # Removes 2, stack is now [1]
print(top_item)  # Output: 2


# frist- frist-out
from collections import deque

q = deque()
q.append(1)  # Queue: [1]
q.append(2)  # Queue: [1, 2]
front_item = q.popleft()  # Removes 1, queue is now [2]
print(front_item)  # Output: 1