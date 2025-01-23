import numpy as np
import random

def generate_equation():
    # Generate x with Gaussian distribution around 0
    while True:
        x = int(np.random.normal(0, 10))
        if -30 <= x <= 30:
            break
    
    # Generate a with constraints
    while True:
        if x == 0:
            a = int(np.random.normal(0, 10))
            if a != 0 and -20 <= a <= 20:
                break
        else:
            max_aval = min(20, 120 // abs(x))
            if max_aval == 0:
                continue
            sigma_a = max(1, max_aval // 2)
            a = int(np.random.normal(0, sigma_a))
            if a != 0 and -max_aval <= a <= max_aval:
                break
    
    # Choose equation structure (1: ax + b = c; 2: ax = b + c)
    structure = random.choice([1, 2])
    
    # Generate constants b and c based on structure
    a_times_x = a * x
    if structure == 1:
        # Structure: ax + b = c
        b_min = max(-100, -100 - a_times_x)
        b_max = min(100, 100 - a_times_x)
        b = np.random.randint(b_min, b_max + 1)
        c = b + a_times_x
    else:
        # Structure: ax = b + c
        b_min = max(-100, a_times_x - 100)
        b_max = min(100, a_times_x + 100)
        b = np.random.randint(b_min, b_max + 1)
        c = a_times_x - b
    
    # Format variable part (a)
    if a == 1:
        var_part = "x"
    elif a == -1:
        var_part = "-x"
    else:
        var_part = f"{a}x"
    
    # Build equation parts
    if structure == 1:
        # Structure: ax + b = c
        if b == 0:
            left = var_part
        else:
            if b > 0:
                left = f"{var_part} + {b}"
            else:
                left = f"{var_part} - {abs(b)}"
        right = str(c)
    else:
        # Structure: ax = b + c
        left = var_part
        # Format right side (b + c)
        terms = []
        if b != 0:
            terms.append(b)
        if c != 0:
            terms.append(c)
        parts = []
        for i, term in enumerate(terms):
            if i == 0:
                parts.append(f"{term}" if term > 0 else f"-{abs(term)}")
            else:
                parts.append(f"+ {term}" if term > 0 else f"- {abs(term)}")
        right = ' '.join(parts) if parts else "0"
    
    equation = f"{left} = {right}"
    
    # Post-process to remove any + - or - + patterns
    equation = equation.replace("+ -", "- ")
    equation = equation.replace("- +", "- ")
    equation = equation.replace("+-", "-")
    
    return equation

# 示例输出
print(generate_equation())