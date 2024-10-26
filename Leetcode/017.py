#给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
#给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
# 输入："23"
# 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

def combination(key1:int,key2:int)->list:
    dict1 = {
        2: ['a', 'b', 'c'],
        3: ['d', 'e', 'f'],
        4: ['g', 'h', 'i'],
        5: ['j', 'k', 'l'],
        6: ['m', 'n', 'o'],
        7: ['p', 'q', 'r', 's'],
        8: ['t', 'u', 'v'],
        9: ['w', 'x', 'y', 'z']
    }
    result=[]
    for i in range(len(dict1[key1])):
        for j in range(len(dict1[key2])):
            string1=dict1[key1][i]+dict1[key2][j]
            result.append(string1)
    return result

print(combination(2,3))
