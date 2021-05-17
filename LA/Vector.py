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
        return Vector([k * e for e in self])

    def __rmul__(self, k):
        '''向量乘法'''
        return self * k

    def __pos__(self):
        '''向量取正'''
        return 1 * self

    def __neg__(self):
        '''向量取负'''
        return -1 * self
