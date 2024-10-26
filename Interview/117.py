# 自动关闭文件
with open('example.txt', 'w') as f:
    f.write("This is an example.")

# 自定义上下文管理器
class ManagedFile:
    def __enter__(self):
        self.file = open('example.txt', 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with ManagedFile() as f:
    f.write("Hello World!")
