from LA.Matrix import Matrix

if __name__ == "__main__":
    matrix = Matrix([[1, 2], [3, 4]])
    print(matrix)
    print(matrix.shape())
    print(matrix.size())
    print(len(matrix))
    print(matrix[0, 0])
    print(matrix.row_vector(0))
    print(matrix.col_vector(0))
    matrix2 = Matrix([[5, 6], [7, 8]])
    print(matrix2 - matrix)
    print(matrix * 2)
    print(2 * matrix)
    print(matrix / 2)
    print(Matrix.zero(3, 7))
