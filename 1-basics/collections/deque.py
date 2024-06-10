from collections import deque

d = deque()

d.append(1)
d.append(2)

d.appendleft(3)
d.pop()
d.clear()
d.extend([4,5,4])
d.rotate(1) # 1 place to right
print(d)