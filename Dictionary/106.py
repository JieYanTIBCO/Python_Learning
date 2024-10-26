from collections import defaultdict

# 定义多层字典
tree = lambda: defaultdict(tree)
nested_dict = tree()

# 添加一些值
nested_dict['level1']['level2']['level3'] = 'deep_value'

print(nested_dict)
