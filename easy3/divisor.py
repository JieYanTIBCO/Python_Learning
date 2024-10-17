import math


def is_divisible(s, t):  # type: ignore
    return s == t * (len(s) // len(t))


s = "ababab"
t = "abab"

print(f"y={y}")

print(is_divisible(s, t))

print(s*2)


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Function to check if one string is a repeated version of another
        def is_divisible(s, t):
            return s == t * (len(s) // len(t))

        # Find the greatest common divisor of the lengths
        gcd_length = math.gcd(len(str1), len(str2))


def is_divisible(s, t):
    return s == t * (len(s) // len(t))
