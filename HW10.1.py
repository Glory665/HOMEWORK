from itertools import zip_longest


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return str('\n'.join(['\t'.join([str(i) for i in j]) for j in self.matrix]))

    def __add__(self, other):
        return Matrix([map(sum, zip_longest(*t, fillvalue=0))
                       for t in zip_longest(self.matrix, other.matrix, fillvalue=[])])


a = [[1, 2], [3, 4], [5, 6]]
b = [[7, 8], [9, 10], [11, 12]]

matrix_1 = Matrix(a)
matrix_2 = Matrix(b)

print(f'Matrix 1:\n{matrix_1}')
print(f'Matrix 2:\n{matrix_2}')
print(f'суммы matrix 1 и matrix 2:\n{matrix_1 + matrix_2}')
