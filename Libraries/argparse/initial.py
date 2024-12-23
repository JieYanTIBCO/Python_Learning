import argparse


parser = argparse.ArgumentParser(description="这是一个命令行参数示例程序")

parser.add_argument("name", help="The first parameter is:用户的名字")  # 必须参数
parser.add_argument("--age", type=int, help="用户的年龄", default=18)  # 可选参数，带默认值
parser.add_argument("--verbose", action="store_true", help="是否启用详细模式")  # 布尔开关

args = parser.parse_args()
print(f"姓名: {args.name}")
print(f"年龄: {args.age}")
if args.verbose:
    print("详细模式已启用")
