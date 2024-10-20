from collections import deque

nums=[1, 12, -5, -6, 50, 3,4,2,54,6,7,213,3]

print(nums[4:])
str="1234567890"
print(str[:5])

window = deque(maxlen=4)

for i in nums:
    window.append(i)
    print(window)