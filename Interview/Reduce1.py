from functools import reduce
import copy

def odd_multiper(a:list):
    odd_multiper = reduce(lambda x, y: x * (y if y % 2 != 0 else 1), a, 1)
    if ( 1 not in a and -1 not in a) and odd_multiper == 1:
        return None
    else:
        return odd_multiper


a = [2, 4, 6]
b = [2, 3, 4, 5, 6]
c = [7, -1, 2, 0, 9, -3, 4, 6]


print(odd_multiper(a))
print(odd_multiper(b))
print(odd_multiper(c))



# a = [1, 2, 3, 4, 5]

# sum_of_element = reduce(lambda x, y: x + y, a)

# print(sum_of_element)


# b = [1, 5, 2, 9, 7, 3]

# # 使用 reduce 找出列表中的最大值
# max_value = reduce(lambda x, y: x if x > y else y, b)

# print(f"列表中的最大值:{max_value}")