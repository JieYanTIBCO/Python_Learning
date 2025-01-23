import random

# Generate a random coefficient for x
a = random.randint(-20, 20)

# Generate a random constant term
b = random.randint(-100, 100)

# Generate a random variable term
c = random.randint(-50, 50)

# Create the equation
equations = ["x^2 + {}x - {} = 0".format(a, b, c)]

# Print the generated equation
print(equations[random.randint(0, len(equations) - 1)])

