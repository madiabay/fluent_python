# this is without typing
from collections import namedtuple
RectangleBox = namedtuple('RectangleBox', 'x y z')

print(issubclass(RectangleBox, tuple))

box1 = RectangleBox(1,2,3)
print(box1)

print(RectangleBox(1,2,3) == box1)
print()


# this is with typing
import typing

Coordinate = typing.NamedTuple('Coordinate', [('lat', float), ('lon', float)])
print(issubclass(Coordinate, tuple))

print(typing.get_type_hints(Coordinate))