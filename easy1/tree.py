import time
import os
from colorama import init, Fore, Back, Style
import random


def clear_screen():
    """Clear the terminal screen."""
    os.system('clear' if os.name == 'posix' else 'cls')


def draw_firework(x: int, y: int) -> list[str]:
    """Draw a firework at given position."""
    patterns = ['*', '+', '×', '✦', '✺', '✹']
    return [random.choice(patterns) for _ in range(3)]


def draw_christmas_tree():
    """Draw an animated Christmas tree with fireworks."""
    init()  # Initialize colorama
    tree_height = 15

    while True:
        clear_screen()

        # Draw stars and fireworks
        for i in range(40):
            x = random.randint(0, 50)
            if random.random() < 0.1:
                print(Fore.YELLOW + '*' + Style.RESET_ALL, end='')
            else:
                print(' ', end='')
        print()

        # Draw the tree
        for i in range(tree_height):
            # Spaces before the tree
            print(' ' * (tree_height - i), end='')

            # Tree branches with decorations
            for j in range(2 * i + 1):
                if random.random() < 0.1:
                    # Ornaments
                    color = random.choice([Fore.RED, Fore.BLUE, Fore.YELLOW])
                    print(color + 'O' + Style.RESET_ALL, end='')
                else:
                    print(Fore.GREEN + '*' + Style.RESET_ALL, end='')
            print()

        # Draw trunk
        print(' ' * tree_height + Fore.BROWN + '|||' + Style.RESET_ALL)
        print(' ' * tree_height + Fore.BROWN + '|||' + Style.RESET_ALL)

        # Draw base
        print(' ' * (tree_height-2) + Fore.RED + '-------' + Style.RESET_ALL)

        # Message
        print("\n" + ' ' * (tree_height-2) + Fore.CYAN +
              "Merry Christmas!" + Style.RESET_ALL)

        time.sleep(0.5)


if __name__ == "__main__":
    try:
        draw_christmas_tree()
    except KeyboardInterrupt:
        print("\nGoodbye!")
