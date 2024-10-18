# li1 = [1, 2, 3]
# li2 = [4, 2, 3]
# li3 = []
# for i in li1:
#     for j in li2:
#         if i != j:
#             li3.append((i, j))
#
# print(li3)
#
# li4 = [(i, j) for i in li1 for j in li2 if i != j]
#
# print(li4)

# جابه جایی سطر و ستون ماتریس
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

matrix1 = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print("Comprehension:")
print(matrix1)

print("Normal:")
matrix2 = []
for i in range(len(matrix[0])):
    t_row = []
    for row in matrix:
        t_row.append(row[i])
    matrix2.append(t_row)

print(matrix2)

print("Function:")
print(list(zip(*matrix)))

