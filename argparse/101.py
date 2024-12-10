import argparse

# 创建解析器
parser = argparse.ArgumentParser(description="这是一个命令行工具示例")

# 添加参数
parser.add_argument("name", type=str, help="用户的名字")
parser.add_argument("-a", "--age", type=int, help="用户的年龄", default=18)
parser.add_argument("-v", "--verbose", action="store_true", help="是否打印详细信息")

# 解析参数
args = parser.parse_args()

# 使用参数
print(f"你好, {args.name}!")
if args.verbose:
    print(f"你今年 {args.age} 岁了。")