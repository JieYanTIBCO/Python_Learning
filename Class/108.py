class ListManager:
    def __init__(self, initial_list=None):
        if initial_list is None:
            initial_list = []
        self.items = initial_list

    def __add__(self, item):
        """Add an item to the list."""
        self.items.append(item)
        return self  # Returning self allows for chaining operations

    def __sub__(self, item):
        """Remove an item from the list."""
        if item in self.items:
            self.items.remove(item)
        else:
            print(f"Item '{item}' not found in the list.")
        return self  # Returning self allows for chaining operations

    def __str__(self):
        """String representation of the list."""
        return f"ListManager({self.items})"

    def get_list(self):
        """Get the current list."""
        return self.items


# Example usage
manager = ListManager(["apple", "banana", "cherry"])
print(manager)
# Add items
manager + "orange" + "pear"
# Output: ListManager(['apple', 'banana', 'cherry', 'orange', 'pear'])
print(manager)

# Remove items
manager - "banana" - ["grape", "pear"]  # 'grape' is not in the list
print(manager)  # Output: ListManager(['apple', 'cherry', 'orange', 'pear'])

# Access the list directly
print(manager.get_list())  # Output: ['apple', 'cherry', 'orange', 'pear']
