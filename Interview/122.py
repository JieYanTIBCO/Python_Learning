import matplotlib.pyplot as plt
import numpy as np

# Define the time range from 0 to 200 seconds for plotting
t_values = np.linspace(0, 200, 200)

# Define the expanded quadratic speed function f(t) = -0.01t^2 + 2t
speed_values = -0.01 * t_values**2 + 2 * t_values

# Plot the speed curve
plt.figure(figsize=(10, 6))
plt.plot(t_values, speed_values, label=r"$f(t) = -0.01t^2 + 2t$", color='blue')
plt.xlabel("Time (seconds)")
plt.ylabel("Speed")
plt.title("Quadratic Speed Curve: Maximum at 100 Seconds, Reaches 0 at 200 Seconds")
plt.grid(True)

# Add reference lines for maximum speed and zero speed points
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(100, color='red', linestyle='--', label="t = 100s (Max Speed)")
plt.axvline(200, color='green', linestyle='--', label="t = 200s (Speed = 0)")
plt.legend()

# Show the plot
plt.show()
