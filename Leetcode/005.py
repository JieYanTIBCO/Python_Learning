class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        max_str = s[0]

        for i in range(len(s) - 1):
            odd = self.expand_from_center(s, i, i)  # 奇数长度回文，以单个字符为中心
            even = self.expand_from_center(s, i, i + 1)  # 偶数长度回文，以两个相邻字符为中心

            if len(odd) > len(max_str):
                max_str = odd
            if len(even) > len(max_str):
                max_str = even

        return max_str

    def expand_from_center(self, s: str, left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

# 测试代码
solution = Solution()
print(solution.longestPalindrome("babad"))  # 输出 "bab" 或 "aba"
print(solution.longestPalindrome("cbbd"))   # 输出 "bb"
print(solution.longestPalindrome("adefeda"))   # 输出 "edefe"



class Solution1:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False] * len(s) for _ in range(len(s))]
        maxlenth = 0
        left = 0
        right = 0
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[j] == s[i]:
                    if j - i <= 1 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                if dp[i][j] and j - i + 1 > maxlenth:
                    maxlenth = j - i + 1
                    left = i
                    right = j
        return s[left:right + 1]

solution1 = Solution1()
print(solution1.longestPalindrome("babad"))  # 输出 "bab" 或 "aba"
print(solution1.longestPalindrome("cbbd"))   # 输出 "bb"
print(solution1.longestPalindrome("adefeda"))   # 输出 "edefede"