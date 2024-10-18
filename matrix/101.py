def create_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    return matrix

matrix= create_matrix(5)
for i in matrix:
    print(i)

print([0]*2)