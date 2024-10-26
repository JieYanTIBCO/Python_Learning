names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
print(enumerate(zip(names, scores)))
# 使用 enumerate() 获取索引和元素，zip() 同时遍历两个列表
for i, (name, score) in enumerate(zip(names, scores)):

    print(f"{i}: {name} scored {score}")


print(ord('a'))
print(chr(97))


fruits = ['apple', 'banana', 'cherry']

# 使用 enumerate 迭代
for fruit in enumerate(*fruits):
    print(fruit)
