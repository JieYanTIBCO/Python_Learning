def longest_unique_substring(s: str) -> str:
    # 验证输入是否为字符串
    if not isinstance(s, str):
        raise TypeError("Input must be a string.")  # 如果输入不是字符串，则抛出类型错误
    
    start = 0  # 滑动窗口的左指针
    max_len = 0  # 记录最长子串的长度
    max_substring = ""  # 记录最长的无重复字符子串
    seen_chars = {}  # 用字典存储每个字符的最后出现的索引位置
    
    # 遍历字符串，`end` 是滑动窗口的右指针
    for end in range(len(s)):
        char = s[end]  # 获取当前字符
        
        # 如果当前字符在`seen_chars`字典中，且位置在当前窗口范围内，则调整左指针 `start`
        if char in seen_chars and seen_chars[char] >= start:
            start = seen_chars[char] + 1  # 将 `start` 移动到重复字符的下一个位置
        
        seen_chars[char] = end  # 更新当前字符的最后出现位置
        
        # 计算当前窗口的长度
        current_len = end - start + 1
        if current_len > max_len:  # 如果当前长度超过了已知的最大长度
            max_len = current_len  # 更新最大长度
            max_substring = s[start:end + 1]  # 更新最长子串的内容
    
    return max_substring  # 返回最长的无重复字符子串


print(longest_unique_substring("abcadefabcfg")) 