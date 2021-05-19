import math
from ._global import EPSILON


class Vector:
    def __init__(self, lst):
        self._values = list(lst)

    def __repr__(self):
        '''Vector([5,2])'''
        return "Vector({})".format(self._values)

    def __str__(self):
        '''(5,2)'''
        return "({})".format(", ".join(str(e) for e in self._values))

    def __len__(self):
        '''返回向量长度'''
        return len(self._values)

    def __getitem__(self, index):
        '''取出向量的第index个元素'''
        return self._values[index]

    def __iter__(self):
        '''返回向量迭代器'''
        return self._values.__iter__()

    def __add__(self, another):
        '''向量加法'''
        assert len(self) == len(another), \
            "Error in adding. Length of vectors must be same."
        return Vector([a + b for a, b in zip(self, another)])

    def __sub__(self, another):
        '''向量减法'''
        assert len(self) == len(another), \
            "Error in subtracting. Length of vectors must be same."
        return Vector([a - b for a, b in zip(self, another)])

    def __mul__(self, k):
        '''向量乘法'''
        try:
            if isinstance(k, int) is not True:
                k = float(k)
            return Vector([k * e for e in self])
        except Exception:
            if len(k) == 1:
                return self * k[0]
            assert len(self) == len(k), \
                "Error in subtracting. Length of vectors must be same."
            return self.dot(k)

    def __rmul__(self, k):
        '''向量乘法'''
        return self * k

    def __pos__(self):
        '''向量取正'''
        return 1 * self

    def __neg__(self):
        '''向量取负'''
        return -1 * self

    @classmethod
    def zero(cls, dim):
        '''返回dim维度零向量'''
        return cls([0] * dim)

    def norm(self):
        '''返回向量的长度'''
        return math.sqrt(sum(e * e for e in self))

    def normalize(self):
        '''返回向量的单位向量'''
        if self.norm() < EPSILON:
            return self.zero(len(self))
            # raise ZeroDivisionError('Normalize error! norm is zero.')
        return Vector(self._values) / self.norm()

    def __truediv__(self, k):
        '''向量数量除法'''
        return (1 / k) * self

    def dot(self, another):
        '''向量点乘'''
        if(len(another) == 1):
            return self * another[0]
        assert len(self) == len(another), \
            "Error in dot product. Length of vectors must be same."
        return sum(a * b for a, b in zip(self, another))
