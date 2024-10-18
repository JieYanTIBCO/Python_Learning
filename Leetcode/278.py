def isBadVersion(n):
    pass


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n

        while left < right:
            mid = left + (right - left) // 2  # 防止溢出
            if isBadVersion(mid):
                right = mid  # 如果是坏版本，继续向左搜索
            else:
                left = mid + 1  # 如果是好版本，继续向右搜索

        return left  # 当 left 和 right 相遇时，它们指向的就是第一个坏版本
