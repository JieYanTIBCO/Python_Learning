import hashlib

# Function to hash a value to a place in the ring
def hash_fn(value):
    return int(hashlib.md5(value.encode('utf-8')).hexdigest(), 16)

# Consistent hashing class
class ConsistentHashing:
    def __init__(self, nodes=None):
        self.ring = {}
        self.sorted_keys = []
        if nodes:
            for node in nodes:
                self.add_node(node)

    # Add a node to the ring
    def add_node(self, node):
        node_hash = hash_fn(node)
        self.ring[node_hash] = node
        self.sorted_keys.append(node_hash)
        self.sorted_keys.sort()

    # Get the node responsible for the given key
    def get_node(self, key):
        key_hash = hash_fn(key)
        for node_hash in self.sorted_keys:
            if key_hash <= node_hash:
                return self.ring[node_hash]
        return self.ring[self.sorted_keys[0]]  # wrap around

    # Helper function to print the current state of the ring
    def print_ring(self):
        print("\nCurrent state of the ring (node hash -> node):")
        for node_hash in self.sorted_keys:
            print(f'{node_hash} -> {self.ring[node_hash]}')

# Simulating with consistent hashing
nodes = ['Node1', 'Node2', 'Node3']
ch = ConsistentHashing(nodes)

# List to store the input keys and their assignments
keys = []

# Function to input keys and assign them
def input_keys():
    while True:
        key = input("Please enter a key (or type 'exit' to stop): ")
        if key.lower() == 'exit':
            break
        assigned_node = ch.get_node(key)
        keys.append((key, assigned_node))
        print(f'Key {key} is assigned to {assigned_node}')

# Start key input
print("Before adding new node:")
input_keys()

# Print the ring before adding the new node
ch.print_ring()

# Print the list of key assignments before adding the new node
print("\nKey assignments before adding new node:")
for key, node in keys:
    print(f'Key {key} was assigned to {node}')

# Adding a new node
ch.add_node('Node4')

# Print the ring after adding the new node
ch.print_ring()

print("\nAfter adding new node 'Node4':")
# Reassign the previously entered keys to the updated nodes and print
for key, _ in keys:
    assigned_node = ch.get_node(key)
    print(f'Key {key} is now assigned to {assigned_node}')
