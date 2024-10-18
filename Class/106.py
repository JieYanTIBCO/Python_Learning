import sqlite3

# 定义数据库连接


def init_db():
    conn = sqlite3.connect('orders.db')  # 连接到数据库（如果不存在则自动创建）
    cursor = conn.cursor()

    # 创建一个 orders 表，用于存储订单信息
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        order_id INTEGER PRIMARY KEY,
        order_type TEXT,
        amount REAL,
        tax_rate REAL,
        total REAL,
        country TEXT
    )
    ''')

    conn.commit()
    return conn

# 将订单信息插入数据库


def save_order_to_db(conn, order_id, order_type, amount, tax_rate, total, country=None):
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO orders (order_id, order_type, amount, tax_rate, total, country)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (order_id, order_type, amount, tax_rate, total, country))
    conn.commit()

# 从数据库读取所有订单信息


def fetch_all_orders(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM orders')
    return cursor.fetchall()

# 从数据库中查询数据


def search_order(conn, order_id):
    cursor = conn.cursor()
    cursor.execute(
        'SELECT count(1) FROM orders where order_id = ?', (order_id,))
    result = cursor.fetchone()  # 获取查询结果的第一行
    return result[0]  # 返回 count(1) 的结果，表示是否找到订单

# 订单类定义


class Order:
    tax_rate = 0.1  # 类属性，所有订单默认税率为10%

    def __init__(self, order_id, amount):
        self.order_id = order_id  # 订单号
        self.amount = amount      # 订单金额

    def calculate_total(self):
        """计算总金额（含税）"""
        return round(self.amount * (1 + self.tax_rate), 2)

    def print_order(self):
        """打印订单信息"""
        print(f"订单号: {self.order_id}, 总金额: {self.calculate_total()}")

    def save_to_db(self, conn):
        """将订单信息保存到数据库"""
        save_order_to_db(conn, self.order_id, 'Normal',
                         self.amount, self.tax_rate, self.calculate_total())

# 会员订单类定义


class MemberOrder(Order):
    discount_rate = 0.2  # 类属性，会员折扣率为20%

    def calculate_total(self):
        """重写计算总金额方法，考虑会员折扣"""
        discounted_amount = self.amount * (1 - self.discount_rate)
        return round(discounted_amount * (1 + self.tax_rate), 2)

    def save_to_db(self, conn):
        """将会员订单信息保存到数据库"""
        save_order_to_db(conn, self.order_id, 'Member',
                         self.amount, self.tax_rate, self.calculate_total())

# 国际订单类定义


class InternationalOrder(Order):
    international_shipping_fee = 50  # 类属性，国际运费为固定值

    def __init__(self, order_id, amount, country):
        super().__init__(order_id, amount)  # 调用父类的构造函数
        self.country = country              # 订单目的国家

    def calculate_total(self):
        """重写计算总金额方法，考虑国际运费"""
        return round(super().calculate_total() + self.international_shipping_fee, 2)

    def print_order(self):
        """重写订单打印方法，增加国际信息"""
        print(f"订单号: {self.order_id}, 国家: {
              self.country}, 总金额: {self.calculate_total()}")

    def save_to_db(self, conn):
        """将国际订单信息保存到数据库"""
        save_order_to_db(conn, self.order_id, 'International', self.amount,
                         self.tax_rate, self.calculate_total(), self.country)

# # 初始化数据库
# conn = init_db()

# # 创建普通订单
# order1 = Order(1001, 100)
# order1.print_order()
# order1.save_to_db(conn)  # 保存到数据库

# # 创建会员订单
# member_order = MemberOrder(1002, 200)
# member_order.print_order()
# member_order.save_to_db(conn)  # 保存到数据库

# # 创建国际订单
# intl_order = InternationalOrder(1003, 300, "USA")
# intl_order.print_order()
# intl_order.save_to_db(conn)  # 保存到数据库

# # 从数据库中读取并打印所有订单
# orders = fetch_all_orders(conn)
# print("\n数据库中的订单信息：")
# for order in orders:
#     print(order)

# # 关闭数据库连接
# conn.close()


conn2 = init_db()
orders2 = fetch_all_orders(conn2)
print("\n第二次链接数据库并打印完整数据：")
for order in orders2:
    print(order)

order_id=1004
result = search_order(conn2, order_id)
print(result)
print(f"\n找到订单号{order_id}" if result != 0 else f"没有找到订单号{order_id}")

conn2.close()
