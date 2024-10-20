def binary_search(nums, target):
    left = 0
    right = len(nums) - 1  # 初始化 right 指向最后一个元素的索引
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:  # 找到目标，返回索引
            return mid
        if nums[mid] > target:  # mid 的值大于目标，移动 right 指针
            right = mid - 1
        else:  # mid 的值小于目标，移动 left 指针
            left = mid + 1
    return -1  # 如果未找到目标，返回 -1


# 测试
print(binary_search([-1, 0, 3, 5, 9, 12], 9))  # 输出: 4
print(binary_search([-1, 0, 3, 5, 9, 12], 2))  # 输出: -1


def binary_search1(nums, target):
    mid= (len(nums)-1)//2
    if not nums:
        return -1
    elif nums[mid] == target:
        return mid
    
    elif nums[mid] > target:
        return binary_search1(nums[:mid],target)
    elif nums[mid] < target:
        result = binary_search1(nums[mid + 1:], target)
        return result + mid + 1 if result != -1 else -1
    
print(binary_search1([-1, 0, 3, 5, 9, 12], 9))  # 输出: 4
print(binary_search1([-1, 0, 3, 5, 9, 12], 2))  # 输出: -1


def binary_search2(nums, target, left=0, right=None):
    # 如果 right 没有被传入（即为 None），初始化为数组最后一个索引
    if right is None:
        right = len(nums) - 1

    # 如果左指针超过右指针，表示没有找到目标
    if left > right:
        return -1

    # 计算中间位置
    mid = (left + right) // 2

    # 检查中间值是否等于目标值
    if nums[mid] == target:
        return mid
    # 如果中间值大于目标值，搜索左半部分
    elif nums[mid] > target:
        return binary_search2(nums, target, left, mid - 1)
    # 如果中间值小于目标值，搜索右半部分
    else:
        return binary_search2(nums, target, mid + 1, right)


# 测试
print(binary_search2([-1, 0, 3, 5, 9, 12], 9))  # 输出: 4
print(binary_search2([-1, 0, 3, 5, 9, 12], 2))  # 输出: -1
