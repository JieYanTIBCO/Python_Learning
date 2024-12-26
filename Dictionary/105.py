from collections import defaultdict

# 当访问不存在的键时，会自动创建一个默认值
word_count = defaultdict(int)
words = ["apple", "banana", "apple", "orange"]
for word in words:
    word_count[word] += 1

word_count["test111"]

print(word_count)  # Output: {'apple': 2, 'banana': 1, 'orange': 1}


items = [
    ('apple', 'fruit'),
    ('carrot', 'vegetable'),
    ('banana', 'fruit'),
    ('spinach', 'vegetable'),
    ('pear', 'fruit')
]

category_dict = defaultdict(list)

for item, category in items:
    category_dict[category].append(item)

print(category_dict)
print(category_dict.items())

# test = category_dict.pop("vegetable")
# print(category_dict)
# print(type(test))
# print(test)
