import random
from typing import List


class solution:
    # Fisher-Yates Algorithm
    def __init__(self, nums: List[int]):
        self.original = nums.copy()
        self.shuffled = nums.copy()

    def reset(self) -> List[int]:
        return self.original.copy()

    def shuffle(self) -> List[int]:
        # reset the shuffled list
        self.shuffled = self.original.copy()
        # take the index and swith with a random number before index element.
        for i in reversed(range(1, len(self.shuffled))):
            j = random.randint(0, i)
            self.shuffled[i], self.shuffled[j] = self.shuffled[j], self.shuffled[i]
            print(f"i: {i}, j: {j}, self.shuffled: {self.shuffled}")
        return self.shuffled

    def print_reversed_list(self):
        m = len(self.shuffled)
        print(f"Original list: {self.original}")
        print(f"The length of the list is: {m}")
        for i in range(m - 1, 0, -1):
            print(f"index: {i}, self.original[i]: {self.original[i]}")


# test code
nums = [1, 2, 3, 4, 5]

obj = solution(nums)
obj.shuffle()
