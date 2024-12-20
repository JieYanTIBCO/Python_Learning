# 练习1：创建一个学生类，包含以下功能：
# 学生名字、年龄、成绩（语文、数学、英语）。
# 方法：计算平均成绩。

class Student:

    def __init__(self, name: str, age: str, scores: list[int | float]):
        self.name = name
        self.age = age
        self.scores = scores

    def avg_scores(self):
        if len(self.scores) != 3:
            print(f"scores must contains 语文、数学、英语 only")
            return
        avg = float(sum(self.scores)/len(self.scores))
        return round(avg, 2)

    def print_info(self):
        print(
            f"student name:{self.name}\nstudent age:{self.age}\naverage score:{self.avg_scores()}")


student1 = Student("Jackie Yan", "42", [77, 97, 100])

student1.print_info()
