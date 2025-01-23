import random
from random import randint


from typing import List


def rand_num() -> int:
    """Return a random number from 0 to 9 with a non-uniform distribution."""
    weights: List[int] = [1, 2, 10, 10, 10, 10, 10, 10,
                          10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1]
    return random.choices(range(20), weights=weights, k=1)[0]


def print_hailey_quize():
    while True:
        a = rand_num()
        b = rand_num()
        if a + b <= 20:
            print(f"{a:>2} + {b:>2} =   ", end="")
            break
        elif a - b <= 20 and a - b > 0:
            print(f"{a:>2} - {b:>2} =   ", end="")
            break


def main():
    for _ in range(15):
        for _ in range(4):
            print_hailey_quize()
        print()


if __name__ == "__main__":
    main()
    # test rand_num()
    # print(rand_num())
