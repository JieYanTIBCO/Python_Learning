from datetime import datetime, timedelta


class MyDateTime(datetime):
    def __str__(self):
        return self.to_millisecond_format()

    def to_millisecond_format(self):
        """返回 ISO 8601 格式，保留 3 位毫秒"""
        return self.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]

    def add_seconds(self, seconds):
        """增加指定秒数"""
        return MyDateTime.fromtimestamp(self.timestamp() + seconds)

    def to_milliseconds(self):
        """将 microseconds 转换为 milliseconds"""
        return self.microsecond // 1000

    @classmethod
    def from_string(cls, date_str: str, fmt: str = "%Y-%m-%d %H:%M:%S.%f"):
        """从字符串创建 MyDateTime 对象"""
        dt = datetime.strptime(date_str, fmt)
        return cls(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, dt.microsecond)

    @classmethod
    def from_datetime(cls, dt: datetime):
        """从 datetime 对象创建 MyDateTime 对象"""
        return cls(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, dt.microsecond)

    @classmethod
    def now(cls):
        """返回当前时间的 MyDateTime 对象"""
        now = datetime.now()
        return cls(now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)


# Example usage
if __name__ == "__main__":
    # Create MyDateTime from string
    dt_str = MyDateTime.from_string("2025-01-04 09:10:57.123456")
    print(f"Original datetime from string: {dt_str}")
    print(f"Milliseconds: {dt_str.to_milliseconds()}")

    # Add seconds
    dt_added = dt_str.add_seconds(3600)
    print(f"Datetime after adding 3600 seconds: {dt_added}")

    # Create MyDateTime from datetime object
    dt = datetime(2025, 1, 4, 9, 10, 57, 123456)
    my_dt = MyDateTime.from_datetime(dt)
    print(f"Original datetime object: {dt}")
    print(f"MyDateTime object: {my_dt}")

    my_dt_now = MyDateTime.now()
    print(f"Current datetime: {my_dt_now}")

    my_dt_test = my_dt_now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current datetime: {my_dt_test}")
