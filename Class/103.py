
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    @classmethod
    def from_string(cls, date_str):
        year, month, day = map(int, date_str.split("-"))
        return cls(year, month, day)
    
    def display(self):
        return f"{self.year}/{self.month}/{self.day}"
    

date_obj = Date.from_string("1988-05-11")
print(date_obj.display())