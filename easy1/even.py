import random


def even_num(nums):
    l1 = [num for num in nums if num % 2 == 0]
    return sorted(l1)


nums = [5, 2, 8, 1, 4, 9, 12, 7]

print(even_num(nums))


# 列表推导式
list_comp = [x**2 for x in range(10)]
print(list_comp)  # 输出: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 生成器表达式
gen_exp = (x**2 for x in range(10))
print(gen_exp)  # 输出: <generator object <genexpr> at 0x...>
print(list(gen_exp))  # 输出: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

gen_exp2 = (random.randint(0,1) for _ in range(10))

print(gen_exp2)  # 输出: <generator object <genexpr> at 0x...>
list2=list(gen_exp2)
print(list2)  # 输出: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

print(sum(list2))