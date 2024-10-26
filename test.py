import sys

import sys

# 计算各种数据类型的大小
int_size = sys.getsizeof(65535*(10**36))
char_size = sys.getsizeof("t")
str_size = sys.getsizeof("Hello, World!")
list_size = sys.getsizeof([1, 2, 3])
tuple_size = sys.getsizeof((1, 2, 3))
dict_size = sys.getsizeof(dict())
set_size = sys.getsizeof(set())
float_size = sys.getsizeof(3.14159265358979)
bool_size = sys.getsizeof(True)

# 打印结果
print(f"Integer (65535*(10**36)) size: {int_size} bytes")
print(f"Character ('t') size: {char_size} bytes")
print(f"String ('Hello, World!') size: {str_size} bytes")
print(f"List ([1, 2, 3]) size: {list_size} bytes")
print(f"Tuple ((1, 2, 3)) size: {tuple_size} bytes")
print(f"Dictionary ({{'a': 1, 'b': 2}}) size: {dict_size} bytes")
print(f"Set ({{1, 2, 3}}) size: {set_size} bytes")
print(f"Float (3.14159265358979) size: {float_size} bytes")
print(f"Boolean (True) size: {bool_size} bytes")

