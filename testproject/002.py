import multiprocessing
import os

def cpu_stress():
    while True:
        pass

if __name__ == "__main__":
    processes = []
    for _ in range(os.cpu_count()):  # Create processes equal to CPU cores
        p = multiprocessing.Process(target=cpu_stress)
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
