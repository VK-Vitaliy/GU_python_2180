class Matrix:
    def __init__(self, list_of_lists):
        self.matrix = list_of_lists

    def __str__(self):
        str_of_matrix = ''
        for list_of_matrix in self.matrix:
            for el in list_of_matrix:
                str_of_matrix = str_of_matrix + f'\t{el}'
            str_of_matrix = str_of_matrix + '\n'
        return str_of_matrix

    def __add__(self, other):
        result = [[other.matrix[i][j] + self.matrix[i][j] for j in range(len(self.matrix[0]))] for i in
                  range(len(self.matrix))]
        return Matrix(result)


m1 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
m2 = Matrix([[2, 3, 3], [-2, 1, -6], [5, -3, 0]])
print('\tМатрица №1:')
print(m1.__str__())
print('\tМатрица №2:')
print(m2.__str__())
print('Матрица №1 + Матрица №2:')
print(m1 + m2)
