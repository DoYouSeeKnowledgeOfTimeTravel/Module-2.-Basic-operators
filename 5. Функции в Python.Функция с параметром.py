# def get_matrix(n, m, value):
#     matrix = []
#     for strk in range(n):
#         stroke = [value] * m
#         matrix.append(stroke)
#     return matrix
#
# result1 = get_matrix(2, 2, 10)
# result2 = get_matrix(3, 5, 42)
# result3 = get_matrix(4, 2, 13)
# print(result1)
# print(result2)
# print(result3)

def get_matrix(n, m, value):
    matrix = []
    for strk in range(n):
        matrix.append([])
        for clmn in range(m):
            matrix[strk].append(value)
    return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
