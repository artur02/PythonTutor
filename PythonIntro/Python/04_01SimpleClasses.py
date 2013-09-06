from abc import ABCMeta
from abc import abstractmethod

# A SIMPLE CLASS

class Counter(object):
    def __init__(self):
        self._count = 0

    def increment(self):
        self._count += 1

    def decrement(self):
        self._count -=1

    #def __str__(self):
    #    return str(self._count)


if __name__ == "__main__":
    counter1 = Counter()
    counter2 = Counter()

    counter1.increment()
    counter1.increment()
    counter1.decrement()
    counter2.decrement()
    counter2.decrement()
    counter2.decrement()
    counter1.increment()

    print("counter1: ", counter1)
    print("counter2: ", counter2)