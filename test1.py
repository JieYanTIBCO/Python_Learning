import sys


dict_size = sys.getsizeof(dict())
set_size = sys.getsizeof(set())

print(f"Dictionary empty ({{}}) size: {dict_size} bytes")
print(f"Set empty({{}}) size: {set_size} bytes")