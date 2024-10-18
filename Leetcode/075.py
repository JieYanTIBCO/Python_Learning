# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
def guess(num: int) -> int:
    # 这个是预定义的函数，不需要自己实现。
    pass


class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2  # 防止整数溢出
            result = guess(mid)
            if result == 0:  # mid is picked number
                return mid
            elif result == 1:  # mid is lower than picked number
                left = mid + 1
            else:  # result == -1 mid is higher than picked number
                right = mid - 1
