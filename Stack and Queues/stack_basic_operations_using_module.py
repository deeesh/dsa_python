# Using Collections module we can easily use class deque() to create stack

import collections
stack = collections.deque()
print(stack)
stack.append(10)
stack.append(20)
stack.append(30)
print(stack)
print(stack[-1])
stack.pop()

# Using Queue module and LifoQueue class we can create stack module
# But instead of append() and pop() we have put() --> To add elements in stack and get() --> To pop elements out of stack

import queue
stack = queue.LifoQueue(2)
stack.put(10)
stack.put(20)
print(stack.get())