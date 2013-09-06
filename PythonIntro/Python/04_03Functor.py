from collections.abc import Callable

# Direction enumeration
class Direction:
    (Up, Down) = range(2)

# Functor
# ~ First class function
class IntComparator(Callable):
    def __init__(self, dir=Direction.Up):
        self._dir=dir

    def __call__(self, *args, **kwds):
        return args[0]<args[1] if self._dir == Direction.Up else args[0]>args[1]


# Insertion sorter
class Sorter(object):
    def __init__(self, items, comparator):
        self._items = items
        self._comp = comparator

    def Sort(self):
        for i in range(len(self._items)):
            valueToInsert = self._items[i]
            holePos = i
            #while holePos >0 and valueToInsert< self.items[holePos-1]:
            while holePos >0 and self._comp(valueToInsert, self._items[holePos-1]):
                self._items[holePos] = self._items[holePos-1]
                holePos  -= 1
            self._items[holePos] = valueToInsert

        return self._items

if __name__ == "__main__":
    items = [3,7,4,9,5,2,6,1]
    print("items: ", items)

    sorter = Sorter(list(items), IntComparator())
    result = sorter.Sort()
    print("items up: ", result)

    sorter2 = Sorter(list(items), IntComparator(Direction.Down))
    result2 = sorter2.Sort()
    print("items down: ",result2)