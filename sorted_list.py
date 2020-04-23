class SimpleList:
    """A program to model a simple list"""

    def __init__(self,items):
        self.items = list(items)

    def add(self,item):
        self.items.append(item)

    def __len__(self):
        return len(self.items)

    def sort(self):
        self.items.sort()

    def __getitem__(self,idx):
        return self.items[idx]

    def __repr__(self):
        return f"SimpleList({self.items})"


class SortedList(SimpleList):

    def __init__(self,items=()):
        super().__init__(items)
        self.sort()

    def add(self,item):
        super().add(item)
        self.sort()

    def __repr__(self):
        return f"SortedList({list(self)})"

class IntList(SimpleList):
    
    def __init__(self,items=()):
        for x in items: self._validate(x)
        super().__init__(items)

    @staticmethod
    def _validate(x):
        if not isinstance(x,int):
            raise TypeError("List only supports integer values")

    def add(self,item):
        self._validate(item)
        super().add(item)

    def __repr__(self):
        return f"List({list(self)})"


class SortedIntList(SortedList,IntList):

    def __init__(self, items=()):
        super().__init__(items=items)

    def __repr__(self):
        return f"SortedIntList({list(self)})"