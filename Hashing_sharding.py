
hashvalue= int('b1ffb6b5d22cd9f210fbc8b7fdaf0e19',16)
divisor = 4
a= hashvalue % divisor

print(f'hashed int value {hashvalue} by {divisor} is equals to {a}, so this part of sharding will be store in node {a}')


# Demonstration of simple modulus-based hashing and its impact when adding/removing a node

# Simulating the simple modulus-based hashing with 4 nodes
hashvalue = int('b1ffb6b5d22cd9f210fbc8b7fdaf0e19', 16)

# Initial setup with 4 nodes
divisor = 4
node_4 = hashvalue % divisor

# New setup with 5 nodes
new_divisor = 5
node_5 = hashvalue % new_divisor

# Print the results
print(f'With 4 nodes, the data is assigned to node {node_4}')
print(f'With 5 nodes, the data is assigned to node {node_5}')


