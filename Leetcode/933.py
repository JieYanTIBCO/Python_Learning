from collections import deque


class RecentCounter:
    def __init__(self):
        self.q1 = deque()
    # [1,100,3001,3002]

    def ping(self, t: int) -> int:  # input the t and return the the number in last 3000ms
        # after invocation, add the t into q1 first.
        self.q1.append(t)
# loop to check if is over 3000ms window, if it is, then left pop until not over
# 3000ms window
        while (t - 3000) > self.q1[0]:
            self.q1.popleft()

        return len(self.q1)




counter = RecentCounter()
print(counter.ping(1))     # 输出: 1
print(counter.ping(100))   # 输出: 2
print(counter.ping(3001))  # 输出: 3
print(counter.ping(3002))  # 输出: 3
