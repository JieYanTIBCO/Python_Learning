import heapq

heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)
print(heap)  # 输出: [1, 3, 2] (最小值在堆的根位置)

nums = [3, 1, 4, 1, 5, 9]
heapq.heapify(nums)
print(nums)

nums = [5, 7, 9, 1, 3]
print(heapq.nlargest(3, nums))  # 输出: [9, 7]
print(heapq.nsmallest(2, nums))  # 输出: [1, 3]