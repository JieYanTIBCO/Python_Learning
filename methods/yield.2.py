import sys

# 普通函数返回 1M 个数字


def create_large_list(n):
    return [i for i in range(n)]

# 生成器返回 1M 个数字


def create_large_generator(n):
    for i in range(n):
        yield i


# 测试 1M 个数字
N = 1_000_000

# 测试列表占用的内存
large_list = create_large_list(N)
print(f"List size in memory: {sys.getsizeof(large_list)} bytes")  # 列表对象的内存占用

# 测试生成器占用的内存
large_generator = create_large_generator(N)
print(f"Generator size in memory: {
      sys.getsizeof(large_generator)} bytes")  # 生成器对象的内存占用

# 遍历生成器，检查其生成的值（惰性计算）
print("Iterating generator:")
for i, value in enumerate(large_generator):
    if i >= 1_000:  # 测试前 5 个值即可
        break
    print(value)

# 生成器消耗的内存是动态的，不会一次性加载所有数据到内存
