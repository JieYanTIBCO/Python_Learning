from pickle import FALSE


class Solution:
    def isValid(self, s1: str) -> bool:
        lst = []
        dict1 = {"]": "[", ")": "(", "}": "{"}
        for i in s1:
            if i in dict1.values():
                lst.append(i)
            elif i in dict1.keys():
                # close bracket situation, empty lst or pop != dict[i]
                if not lst or lst.pop() != dict1[i]:
                    return False
        if not lst:
            return True
        else:
            return False


obj = Solution()
print(obj.isValid("[{()}](){}"))
