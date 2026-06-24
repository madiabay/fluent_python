# annotating just for documentation and IDE, not for python
import typing

class Coordinate(typing.NamedTuple):
    lat: float
    lon: float

trash = Coordinate('Trsash!', None)

print(trash)
print()



class DemoPlainClass:
    a: int
    b: float = 1.1
    c = 'spam'

print(DemoPlainClass.__annotations__)

try:
    print(DemoPlainClass.a)
except Exception as e:
    print(e)
print(DemoPlainClass.b)
print(DemoPlainClass.c)
print()


class DemoNTClass(typing.NamedTuple):
    a: int
    b: float = 1.1
    c = 'spam'


print(DemoNTClass.__annotations__)
print(DemoNTClass.a)
print(DemoNTClass.b)
print(DemoNTClass.c)
print(DemoNTClass.__doc__)
print()

nt = DemoNTClass(8)

print(nt.a)
print(nt.b)
print(nt.c)
nt.a = 123 # error