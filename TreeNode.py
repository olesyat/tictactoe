class Node:
    def __init__(self, data,_0=None, _1=None, _2=None, _3=None, _4=None, _5=None, _6=None, _7=None):
        self.data = data
        self._0 = _0
        self._1 = _1
        self._2 = _2
        self._3 = _3
        self._4 = _4
        self._5 = _5
        self._6 = _6
        self._7 = _7
        self.generation = 0
        self._all = [self._0,
                     self._1,
                     self._2,
                     self._3,
                     self._4,
                     self._5,
                     self._6,
                     self._7]
        self.chances = 0
        self.ancestor = None

    def add_child(self, data):
        for i in range(8):
            if self._all[i] is None:
                self._all[i] = Node(data)
                self._all[i].ancestor = self
                break

    def count_chances(self):
        pass


    def __str__(self):
        result = str(self.data) + '\n'
        for e in self._all:
            if e:
                result += str(e) + '\n'
        return result

