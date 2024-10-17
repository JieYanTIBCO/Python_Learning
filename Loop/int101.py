import time
def count_times(n: int) -> int:
    count = 0
    while n > 1:
        if n & 1 == 0:
            n = n // 2  # Using integer division
        else:
            n += 1
        count += 1
    return count

start_time=time.time()
n=501023142579841213462465457
print(f"The number {n} will be manipulated: {count_times(n)} times to get 1")

end_time=time.time()

execution_time=end_time-start_time
print(f"start time:{start_time}")
print(f"start time:{end_time}")
print(f"Execution Time: {execution_time:.6f} seconds")