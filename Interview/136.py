import pandas as pd
import sqlite3

db_path = r"C:\Users\Jackie\AppData\Roaming\DBeaverData\workspace6\.metadata\sample-database-sqlite-1\Chinook.db"

# 连接到 SQLite 数据库
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# 查询数据库
cursor.execute("select * from Employee;")
Employee_table = cursor.fetchall()
for row in Employee_table:
    print(row)
print(type(Employee_table))

conn.close

# # 读取 CSV 文件为 DataFrame
# df = pd.read_csv("data.csv")


# # 将数据导入数据库
# df.to_sql("people", conn, if_exists="replace", index=False)

# # 关闭连接
# conn.close()

# print("CSV 数据已成功通过 Pandas 导入到数据库！")
