# Created using Queue module or collections
import collections
q = collections.deque()
print(q)
q.appendleft(10)
q.appendleft(20)
q.appendleft(30)
# appending from one side (i.e left at this moment)
print(q)
q.pop()
print(q)
q.pop()
print(q)