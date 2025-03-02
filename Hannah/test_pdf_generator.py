import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from pdf_generator import PDFGenerator

# 测试方程组和解
equations = [
    "x + y = 10",
    "2x - y = 5",
    "3x + 2y = 20",
    "x - y = 1",
    "5x + 3y = 25"
]

solutions = [
    "x=5, y=5",
    "x=3, y=1",
    "x=4, y=4",
    "x=2, y=1",
    "x=5, y=0"
]

# 创建PDF生成器实例
output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "test_output.pdf")
pdf_gen = PDFGenerator(output_path, num_columns=2, equations_per_column=3)

# 生成PDF
pdf_gen.generate_pdf(equations, solutions)

print("PDF生成成功，请查看test_output.pdf文件")
