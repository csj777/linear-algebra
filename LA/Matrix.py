from .Vector import Vector


class Matrix:
    def __init__(self, list2d):
        self._values = [row[:] for row in list2d]

    def __repr__(self):
        return "Matrix({})".format(self._values)

    __str__ = __repr__

    def row_num(self):
        '''返回矩阵行数'''
        return self.shape()[0]

    __len__ = row_num

    def col_num(self):
        '''返回矩阵列数'''
        return self.shape()[1]

    def shape(self):
        '''矩阵形状：（行，列）'''
        return len(self._values), len(self._values[0])

    def size(self):
        r, c = self.shape()
        return r * c

    def __getitem__(self, pos):
        '''返回pos位置元素'''
        r, c = pos
        return self._values[r][c]

    def row_vector(self, index):
        '''返回矩阵第index个行向量'''
        return Vector(self._values[index])

    def col_vector(self, index):
        '''返回矩阵第index个列向量'''
        return Vector([row[index] for row in self._values])

    def __add__(self, another):
        '''矩阵相加'''
        assert self.shape() == another.shape(), \
            "Error in adding. Shape of matrix must be same."
        return Matrix([[
            a + b for a, b in zip(self.row_vector(i), another.row_vector(i))
        ] for i in range(self.row_num())])

    def __sub__(self, another):
        '''矩阵相加'''
        assert self.shape() == another.shape(), \
            "Error in subtracting. Shape of matrix must be same."
        return Matrix([[
            a - b for a, b in zip(self.row_vector(i), another.row_vector(i))
        ] for i in range(self.row_num())])

    def __mul__(self, k):
        '''矩阵数量乘法：self * k'''
        return Matrix([[e * k for e in self.row_vector(i)]
                       for i in range(self.row_num())])

    def __rmul__(self, k):
        '''矩阵数量乘法：k * self'''
        return Matrix([[e * k for e in self.row_vector(i)]
                       for i in range(self.row_num())])

    def __truediv__(self, k):
        '''矩阵数量除法：self / k'''
        return (1 / k) * self

    def __pos__(self):
        '''矩阵取正'''
        return 1 * self

    def __neg__(self):
        '''矩阵取负'''
        return -1 * self

    @classmethod
    def zero(cls, r, c):
        '''返回r行c列零矩阵'''
        return cls([[0] * c for _ in range(c)])