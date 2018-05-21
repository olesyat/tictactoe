class Node:
    def __init__(self, data, _0=None, _1=None, _2=None, _3=None, _4=None, _5=None, _6=None, _7=None, _8=None):
        self.data = data
        # self._0 = _0
        # self._1 = _1
        # self._2 = _2
        # self._3 = _3
        # self._4 = _4
        # self._5 = _5
        # self._6 = _6
        # self._7 = _7
        # self._8 = _8
        self._all = [None for i in range(9)]

    def add_child(self, data):
        for i in range(9):
            if self._all[i] is None:
                self._all[i] = data
                break

    def __str__(self):
        result = ''
        for e in self._all:
            if e:
                result += str(e)
        return result