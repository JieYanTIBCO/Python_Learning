import argparse
import sqlite3

parser = argparse.ArgumentParser(description="这是一个参数传递示例程序")
parser.add_argument("name", help="输入用户姓名")
parser.add_argument("--age", type=int, help="输入年龄", default=30)  # 带默认值的参数
parser.add_argument("--verbose", action="store_true", help="启用详细模式")  # 开关参数

args = parser.parse_args()

# create connection to local database example.db
connection = sqlite3.connect("exmaple.db")
# create cursor of this connection
cursor = connection.cursor()

# Create user table if it does not exist
create_table_ddl = """
Create table users(
    userid integer primary key AUTOINCREMENT,
    name text not null,
    age integer not null
    )
"""
cursor.execute(create_table_ddl)

# insert the record according to the input
insert_query = "insert into users(name,age) values(?,?)"
cursor.execute(insert_query, (args.name, args.age))
connection.commit()

# Step 3: Retrieve a value from the table
select_query = "SELECT * FROM users"
cursor.execute(select_query)
result = cursor.fetchone()  # Fetch one result
if result:
    print(f"Name: {result[0]}, Age: {result[1]}")
else:
    print("No record found")

connection.close()

print(f"姓名: {args.name}")
print(f"年龄: {args.age}")
if args.verbose:
    print("详细模式已启用")
