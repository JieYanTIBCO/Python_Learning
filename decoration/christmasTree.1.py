import random
import os
import time


def print_colored(text: str, color: str) -> str:
    """Return colored text using ANSI escape codes."""
    colors = {
        'red': '\033[91m',
        'light_red': '\033[90m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'light_yellow': '\033[90m',
        'brown': '\033[38;5;94m',
        'dark_brown': '\033[38;5;52m',
        'white': '\033[97m',
        'blue': '\033[94m',
        'reset': '\033[0m'
    }
    return f"{colors.get(color, '')}{text}{colors['reset']}"


def generate_sky_elements(size: int, density: float) -> list:
    """Generate random positions for stars in the sky."""
    positions = []
    for row in range(10):  # 10 rows of sky
        positions.append(random.sample(range(size), int(size * density)))
    return positions


def print_fixed_sky(size: int, stars: list, moon_pos: int) -> None:
    """Print the sky with fixed stars and a fixed moon."""
    for row in range(10):  # Fixed 10 rows of sky
        line = [" "] * size

        # Add fixed moon
        if row == 2 and moon_pos < size - 3:
            for i, char in enumerate("🌙"):
                line[moon_pos + i] = char

        # Add stars
        for star_pos in stars[row]:
            if star_pos < size:
                line[star_pos] = print_colored("✨", 'white')

        print("".join(line))


def print_tree_pattern(size: int, snow_density: float = 0.15, toggle: bool = True) -> None:
    """Print a Christmas tree with static leaves and flashing decorations."""
    if size % 2 == 0:
        size += 1

    # Print the star
    print(" " * (size // 2) + print_colored("⭐", 'yellow'))

    # Print tree
    for i in range(1, size, 2):
        spaces = (size - i) // 2
        line = [" "] * size

        # Generate tree row with decorations
        for j in range(i):
            if i <= 3:  # Top two rows
                line[spaces + j] = print_colored("*", 'green')
            elif j == 0 or j == i - 1:  # Left and right edge decorations
                if (i // 2) % 2 == 1:  # Flashing red decorations
                    line[spaces + j] = print_colored(
                        "O", 'red') if toggle else print_colored("o", 'light_red')
                else:  # Flashing yellow decorations
                    line[spaces + j] = print_colored(
                        "@", 'yellow') if toggle else print_colored("@", 'light_yellow')
            else:  # Tree leaves
                line[spaces + j] = print_colored("*", 'green')

        # Add snowflakes
        for snow_pos in range(size):
            if random.random() < snow_density and line[snow_pos] == " ":
                line[snow_pos] = print_colored("❄", 'white')

        print("".join(line))


def print_trunk_and_reindeer(size: int) -> None:
    """Print the tree trunk and a reindeer beside the tree."""
    trunk_width = size // 6
    trunk_height = trunk_width
    padding = (size - trunk_width) // 2

    for i in range(trunk_height):
        line = [" "] * size
        # Add snow around the trunk
        for _ in range(random.randint(1, 3)):
            snow_pos = random.randint(0, padding - 1)
            line[snow_pos] = print_colored("❄", 'white')
        for _ in range(random.randint(1, 3)):
            snow_pos = random.randint(padding + trunk_width, size - 1)
            line[snow_pos] = print_colored("❄", 'white')

        # Add the trunk
        for j in range(trunk_width):
            line[padding + j] = print_colored("#", 'dark_brown')

        # Add reindeer
        if i == 0:
            line += "     🦌"  # Reindeer head
        elif i == 1:
            line += "    🦌🦌"  # Reindeer body

        print("".join(line))


def generate_gifts(size: int) -> (list, list):
    """Generate fixed positions for gifts and cards below the tree."""
    gift_row_1 = [" "] * size
    gift_row_2 = [" "] * size
    gift_positions = random.sample(range(size), 6)  # Random gift positions
    for pos in gift_positions:
        gift_row_1[pos] = print_colored("🎁", 'red')
        gift_row_2[pos] = print_colored(
            "🎴", 'yellow')  # Replace with greeting card
    return gift_row_1, gift_row_2


def print_fixed_gifts(gift_row_1: list, gift_row_2: list) -> None:
    """Print the fixed gifts and cards."""
    print("".join(gift_row_1))
    print("".join(gift_row_2))


def display_tree_with_reindeer(size: int, snow_density: float = 0.15, stars_density: float = 0.1, iterations: int = 10):
    """Display the tree dynamically with reindeer, changing snow, and flashing decorations."""
    stars = generate_sky_elements(size, stars_density)  # Fixed star positions
    moon_pos = random.randint(0, size - 8)  # Fixed moon position
    gift_row_1, gift_row_2 = generate_gifts(size)  # Generate fixed gifts

    for i in range(iterations):
        os.system("cls" if os.name == "nt" else "clear")

        # Print sky with fixed stars and moon
        print_fixed_sky(size, stars, moon_pos)

        # Print tree
        print_tree_pattern(size, snow_density, toggle=(i % 2 == 0))
        print_trunk_and_reindeer(size)

        # Print fixed gifts
        print_fixed_gifts(gift_row_1, gift_row_2)

        time.sleep(0.5)


def main() -> None:
    # Parameters
    tree_size = 61
    snow_density = 0.08
    stars_density = 0.05
    iterations = 15

    # Display tree dynamically with a reindeer
    display_tree_with_reindeer(
        tree_size, snow_density, stars_density, iterations)


if __name__ == "__main__":
    main()
