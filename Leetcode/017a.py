def combination(keys: str) -> list:
    dict1 = {
        0: [" "],
        1: [" "],
        2: ['a', 'b', 'c'],
        3: ['d', 'e', 'f'],
        4: ['g', 'h', 'i'],
        5: ['j', 'k', 'l'],
        6: ['m', 'n', 'o'],
        7: ['p', 'q', 'r', 's'],
        8: ['t', 'u', 'v'],
        9: ['w', 'x', 'y', 'z']
    }
    if keys == '' or keys == ' ':
        return []
    # 初始化结果列表，开始时设置为空字符串
    result = ['']

    # 遍历输入的每个数字
    for key in keys:
        if int(key) not in dict1.keys():
            print(f"incorrect key:{key}")
            continue
        letters = dict1[int(key)]  # 获取对应的字母列表
        new_result = []
        # 将每个已有的组合与新的字母连接
        for prefix in result:
            for letter in letters:
                new_result.append(prefix + letter)
                # print(prefix)
                # print(letter)
        result = new_result
        # print(result)

    return result


# 示例调用
print(combination("2134"))
print(combination("2"))
print(combination(""))
print(combination(' '))
