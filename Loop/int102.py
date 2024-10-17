import time
import psutil

# Function to check if a number is even using bitwise AND
def is_even_bitwise(n):
    return n & 1 == 0

# Function to check if a number is even using modulus
def is_even_modulus(n):
    return n % 2 == 0

# Function to compare performance and CPU usage
def compare_cpu_performance(loop_count):
    # Measure CPU usage and time for bitwise method
    start_cpu_bitwise = psutil.cpu_percent(interval=None)
    start_time_bitwise = time.time()
    
    for i in range(loop_count):
        is_even_bitwise(i)
    
    end_time_bitwise = time.time()
    end_cpu_bitwise = psutil.cpu_percent(interval=None)
    
    # Measure CPU usage and time for modulus method
    start_cpu_modulus = psutil.cpu_percent(interval=None)
    start_time_modulus = time.time()
    
    for i in range(loop_count):
        is_even_modulus(i)
    
    end_time_modulus = time.time()
    end_cpu_modulus = psutil.cpu_percent(interval=None)
    
    # Calculate time and CPU consumption
    bitwise_time = end_time_bitwise - start_time_bitwise
    bitwise_cpu = end_cpu_bitwise - start_cpu_bitwise
    
    modulus_time = end_time_modulus - start_time_modulus
    modulus_cpu = end_cpu_modulus - start_cpu_modulus
    
    # Print results
    print(f"Bitwise method took: {bitwise_time:.6f} seconds and used {bitwise_cpu}% CPU for {loop_count} iterations")
    print(f"Modulus method took: {modulus_time:.6f} seconds and used {modulus_cpu}% CPU for {loop_count} iterations")

# Compare performance for 1 million iterations
compare_cpu_performance(1000000)
