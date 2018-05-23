class Node:
    def __init__(self, data, ancestor):
        self.data = data
        self.children = []
        self.chance = 0
        self.ancestor = ancestor

    def get_ancestor(self):
        try:
            if self.ancestor.ancestor is not None:
                return self.ancestor.get_ancestor()
            return self
        except:
            return 'ancestor'

    def add_child(self, child):
        self.children.append(child)

    def has_children(self):
        return len(self.children) != 0

    def __str__(self):
        result = str(self.data) + '\n'
        # for e in self.children:
        #     if e:
        #         result += str(e) + '\n'
        return result

    def count_chance(self):
        if self.has_children():
            for child in self.children:
                self.chance += child.count_chance()
        return self.chance


class Tree:
    def __init__(self, root):
        self._root = root
