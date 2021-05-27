from LA.Matrix import Matrix
from LA.Vector import Vector

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

    T = Matrix([[1.5, 0], [0, 2]])
    p = Vector([5, 3])
    P = Matrix([[0, 4, 5], [0, 0, 3]])
    print(T.dot(p))
    print(T.dot(P))
