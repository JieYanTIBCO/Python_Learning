from collections import deque


queue = deque([1, 2, 3, 4])
queue.rotate(-2)
print(queue)
