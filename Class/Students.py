class Students:
    """题目:实现一个学生成绩管理系统
    请设计一个 Student 类，满足以下功能:
    实例属性:
    name:学生姓名（字符串）
    score:学生分数（整数）
    类属性:
    total_students:记录学生总人数
    total_score:记录所有学生的总分
    方法:
    __init__(self, name, score):初始化学生，更新 total_students 和 total_score。
    update_score(self, new_score):修改学生的分数，并同步更新 total_score。
    @classmethod average_score(cls):返回所有学生的平均分（保留两位小数）。
    """

    total_students = 0
    total_score = 0

    def __init__(self, name: str, score: int):
        self.name = name
        self.score = score
        Students.total_students += 1
        Students.total_score += self.score

    def update_score(self, new_score: int):
        old_score = self.score
        self.score = new_score
        Students.total_score += new_score - old_score
        print(
            f"The student {self.name} has updated, the score has been changed from {old_score} to {self.score}"
        )

    def delete_student(self):
        Students.total_students -= 1
        Students.total_score -= self.score
        print(f"The student {self.name} has been deleted")

    @classmethod
    def average_score(cls):
        if cls.total_students == 0:
            return 0.0
        else:
            return round(Students.total_score / Students.total_students, 2)


# test code
student1 = Students("Jackie", 100)
student2 = Students("Tom", 90)
student3 = Students("Jerry", 80)

print(f"student1.name: {student1.name}, student1.score: {student1.score}")
print(f"student2.name: {student2.name}, student2.score: {student2.score}")
print(f"student3.name: {student3.name}, student3.score: {student3.score}")
print(f"Students.total_students: {Students.total_students}")
print(f"Students.total_score: {Students.total_score}")
print(f"Students.average_score(): {Students.average_score()}")

# test update_score
student1.update_score(95)
print(f"student1.name: {student1.name}, student1.score: {student1.score}")
print(f"Students.total_students: {Students.total_students}")
print(f"Students.total_score: {Students.total_score}")
print(f"Students.average_score(): {Students.average_score()}")
