class Vector:
    def __init__(self, lst):
        self._values = lst

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
