# 判断列表中是否全部为正数
nums = [3, 5, 1, 7, -2]
all_positive = all(x > 0 for x in nums)
print(all_positive)  # Output: False

# 判断列表中是否有至少一个偶数
has_even = any(x % 2 == 0 for x in nums)
print(has_even)  # Output: False


arr = [0, 1, 2, 3, 4, 5]
# 反转列表
reversed_arr = arr[::-1]
print(reversed_arr)  # Output: [5, 4, 3, 2, 1, 0]
str = "abcd"
reverse_str = str[::-1]

print(reverse_str)  # Output: "dcba"

skip_elements = arr[::2]
print(skip_elements)  # Output: [0, 2, 4]

skip_elements1 = str[::-2]
print(skip_elements1)  # Output: [a,c]

try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
finally:
    print("This block always executes.")