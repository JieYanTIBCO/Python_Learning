def binary_search(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, high)

# 示例数组和目标值
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 7

# 调用二分查找
result = binary_search(arr, target, 0, len(arr) - 1)

if result != -1:
    print(f"元素 {target} 在索引 {result} 处找到。")
else:
    print(f"元素 {target} 不在数组中。")
