import random

class BingoCage:

    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)
        print(self._items)
    
    def pick(self):
        try:
            print(self._items.pop())
            print(self._items)
            print()
        except IndexError:
            raise LookupError('pick from empty BingoCage')
    
    def __call__(self, *args, **kwds):
        self.pick()


bc = BingoCage({1,2,3,4,5,6,7,8,9,})

bc.pick()

for _ in range(5):
    bc() # using __call__ dunder method


print(bc._items)