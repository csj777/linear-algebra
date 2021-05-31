from LA.Matrix import Matrix
from LA.Vector import Vector
from LA.LinearSystem import LinearSystem
from LA.LinearSystem import inv, rank

if __name__ == "__main__":

    # A = Matrix([[1, 2, 4], [3, 7, 2], [2, 3, 3]])
    # b = Vector([7, -11, 1])
    # A = Matrix([[1, -1, 2, 0, 3], [-1, 1, 0, 2, -5], [1, -1, 4, 2, 4],
    #             [-2, 2, -5, -1, -3]])
    # b = Vector([1, 5, 13, -1])
    # A = Matrix([[2, 2], [2, 1], [1, 2]])
    # b = Vector([3, 2.5, 7])
    # ls = LinearSystem(A, b)
    # if not ls.gauss_jordan_elimination():
    #     print("No Solution!")

    # ls.fancy_print()

    A = Matrix([[1, 2], [3, 4]])
    invA = inv(A)
    print(A.dot(invA))
    print(invA.dot(A))

    print(rank(A))
