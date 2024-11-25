import pandas as pd
import sqlite3

db_path = r"C:\Users\Jackie\AppData\Roaming\DBeaverData\workspace6\.metadata\sample-database-sqlite-1\Chinook.db"

conn = sqlite3.connect(db_path)

# use pandas to export csv
df = pd.read_sql_query("select * from Employee;", conn)

print(df.head(5))
print(df.tail(2))
# df.info()
print(df.dtypes)


# # output csv file
# output_csv = r"C:\Users\Jackie\Employee_export.csv"
# df.to_csv(output_csv, index=False)

# # print(f"Employee 表已导出到 {output_csv}")
conn.close


