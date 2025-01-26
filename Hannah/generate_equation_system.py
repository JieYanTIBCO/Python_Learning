import random
import math
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def generate_valid_equation_system():
    """
    生成格式规范的二元一次方程组，满足以下条件：
    方程格式：
        a1x + b1y = c1
        a2x + b2y = c2

    条件：
    1. 方程解x, y为整数(-20 ≤ x ≤ 20), 且服从高斯分布, 即x，y=0的概率最大。
    2. 系数a1, a2, b1, b2 ∈ [-20, 20]且均为非零整数。
    3. 常数项c1, c2满足：
        a1x + b1y <= 120
        a2x + b2y <= 120
    4. 系数a1, b1, a2, b2服从高斯分布，且满足：
        a = 1时不显示，a = -1时显示为-x或-y。
    5. 方程始终包含变量项，且自动优化显示格式，避免出现--或者+-等情况。
    6. 常量项c1, c2分别位于等式的右侧。
    """

    def weighted_random():
        """使用高斯分布生成服从概率分布的整数值"""
        values = list(range(-20, 21))
        mean = 0
        stddev = 7  # 标准差，越小集中度越高
        weights = [math.exp(-((x - mean) ** 2) / (2 * stddev**2)) for x in values]
        return random.choices(values, weights=weights, k=1)[0]

    def format_term(value, variable):
        """格式化单项式"""
        if value == 0:
            return ""
        if value == 1:
            return variable
        if value == -1:
            return f"-{variable}"
        return f"{value}{variable}"

    while True:
        x = weighted_random()
        y = weighted_random()

        a1 = weighted_random()
        b1 = weighted_random()
        a2 = weighted_random()
        b2 = weighted_random()

        if a1 == 0 or b1 == 0 or a2 == 0 or b2 == 0:
            continue

        c1 = a1 * x + b1 * y
        c2 = a2 * x + b2 * y

        if abs(c1) > 120 or abs(c2) > 120:
            continue

        break

    # 构建方程格式
    equations = [
        f"{format_term(a1, 'x')} + {format_term(b1, 'y')} = {c1}",
        f"{format_term(a2, 'x')} + {format_term(b2, 'y')} = {c2}",
    ]

    # 格式清理优化
    for i in range(len(equations)):
        equations[i] = equations[i].replace("+ -", "- ")
        equations[i] = equations[i].replace("- -", "+ ")
        equations[i] = equations[i].replace(" 1x", " x")
        equations[i] = equations[i].replace(" 1y", " y")

    return equations, (x, y)


def create_pdf(filename, num_columns=3, equations_per_column=10, page_num=1):
    """生成包含方程组的PDF文件
    :param filename: PDF文件名
    :param num_columns: PDF中列数
    :param equations_per_column: 每列显示的方程组数量
    :param page_num: 生成的PDF页数

    生成的PDF文件包含多个页面，每个页面包含多个列，每列包含多个方程组并带有编号。
    在页脚显示整页方程组的解有编号，字体要很小。
    """
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    # 页面设置
    margin = 20
    column_width = (width - 2 * margin) / num_columns
    start_x = margin
    start_y = height - margin
    line_height = 20
    footer_height = 30

    # 存储所有解
    solutions = []
    equations_on_page = 0
    column = 0
    y = start_y

    for idx in range(1, num_columns * equations_per_column + 1):
        equations, solution = generate_valid_equation_system()
        eq1, eq2 = equations
        solutions.append(solution)

        if equations_on_page % equations_per_column == 0 and equations_on_page > 0:
            column += 1
            y = start_y

        if column >= num_columns:
            # 添加页脚解
            c.setFont("Helvetica", 6)
            footer_text = "Solutions: "
            for i, sol in enumerate(solutions[-equations_per_column:]):
                footer_text += f"{i+1}. ({sol[0]}, {sol[1]})  "
            c.drawString(margin, footer_height, footer_text)
            c.showPage()
            column = 0
            y = start_y

        x = start_x + column * column_width
        c.setFont("Helvetica", 10)
        c.drawString(x, y, f"{{ {eq1} }}")
        y -= line_height
        c.drawString(x, y, f"{{ {eq2} }}")
        y -= line_height * 2  # 空一行

        equations_on_page += 1

    # 添加最后一页的页脚解
    c.setFont("Helvetica", 6)
    footer_text = "Solutions: "
    for i, sol in enumerate(solutions[-equations_per_column:]):
        footer_text += f"{i+1}. ({sol[0]}, {sol[1]})  "
    c.drawString(margin, footer_height, footer_text)
    c.save()


if __name__ == "__main__":
    create_pdf("./equations.pdf", num_columns=3, equations_per_column=3, page_num=3)
