from utils.log_decoration import log_decoration
import random


def print_colored(text: str, color: str) -> str:
    """Return colored text using ANSI escape codes."""
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'brown': '\033[38;5;94m',
        'dark_brown': '\033[38;5;52m',
        'white': '\033[97m',
        'reset': '\033[0m'
    }
    return f"{colors.get(color, '')}{text}{colors['reset']}"


def print_trunk(n: int) -> None:
    """Print a dark brown tree trunk with snowflakes around it."""
    trunk_size = round(n / 6)
    trunk_width = trunk_size
    trunk_height = trunk_size
    padding = (n - trunk_width) // 2

    for _ in range(trunk_height):
        line = [" "] * n

        # Add snowflakes randomly on the left and right sides of the trunk
        for _ in range(random.randint(1, 2)):
            snow_pos = random.randint(0, padding - 1)
            line[snow_pos] = print_colored("❄", 'white')

        for _ in range(random.randint(1, 2)):
            snow_pos = random.randint(padding + trunk_width, n - 1)
            line[snow_pos] = print_colored("❄", 'white')

        # Add the trunk
        for i in range(trunk_width):
            line[padding + i] = print_colored("#", 'dark_brown')

        print("".join(line))


def print_tree_pattern(size: int) -> None:
    """Print a Christmas tree with random snowflakes appearing inside and outside the tree."""
    if size % 2 == 0:
        size += 1

    # Print star at the top
    print(" " * (size // 2) + print_colored("⭐", 'yellow'))

    # Print tree
    for i in range(1, size, 2):
        spaces = (size - i) // 2
        line = [" "] * size

        # Generate tree row with decorations
        for j in range(i):
            if i <= 3:
                line[spaces + j] = print_colored("*", 'green')
            elif i == size - 1:
                line[spaces + j] = (
                    print_colored("O", 'red') if j == 0 or j == i -
                    1 else print_colored("*", 'green')
                )
            elif (i // 2) % 2 == 1:
                line[spaces + j] = (
                    print_colored("O", 'red') if j == 0 or j == i -
                    1 else print_colored("*", 'green')
                )
            else:
                line[spaces + j] = (
                    print_colored("@", 'yellow') if j == 0 or j == i -
                    1 else print_colored("*", 'green')
                )

        # Add snowflakes outside the tree (on left and right sides)
        for _ in range(random.randint(1, 3)):
            snow_pos_left = random.randint(0, spaces - 1)
            snow_pos_right = random.randint(spaces + i, size - 1)
            if snow_pos_left < len(line):
                line[snow_pos_left] = print_colored("❄", 'white')
            if snow_pos_right < len(line):
                line[snow_pos_right] = print_colored("❄", 'white')

        # Add snowflakes inside the tree, but avoid decorations
        for snow_pos in range(size):
            if random.random() < 0.15 and line[snow_pos] == print_colored("*", 'green'):
                line[snow_pos] = print_colored("❄", 'white')

        print("".join(line))


@log_decoration()
def main() -> None:
    n = 41  # Tree size
    print_tree_pattern(n)
    print_trunk(n)


if __name__ == "__main__":
    main()
