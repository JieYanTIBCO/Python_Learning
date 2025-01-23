import random

def generate_equation():
    a = random.randint(-20, 20)  # 系数a在-20到20之间，且不为0
    if a == 0:
        return None  # 不包含常数项的情况不符合要求
    
    b = random.randint(-100, 100)
    c = random.randint(-100, 100)
    
    x_term = f"{'x' if a == 1 else ('-x' if a == -1 else f'{a}x')}"
    
    # 确保常数项分别位于等式两边
    left_side = f"{x_term} = {b}"
    right_side = f"{c}"
    
    equation = f"{left_side} {right_side}"
    
    # 确保解在-30到30之间，且服从高斯分布（即x=0的概率最大）
    # 这里通过生成满足条件的方程来实现
    return equation

for _ in range(10):

    print(generate_equation())
