# from dataclasses import dataclass

# @dataclass
# class DemoDataClass:
#     a: int
#     b: float = 1.1
#     c = 'spam'

# print(DemoDataClass.__annotations__)
# print(DemoDataClass.__doc__)

# try:
#     print()
#     print(DemoDataClass.a)
# except Exception:
#     print('error')

# print(DemoDataClass.b)
# print(DemoDataClass.c)
# print()

# dc = DemoDataClass(123)
# dc.a = 321

# print(dc.a)
# print(dc.b)
# print(dc.c)



from dataclasses import dataclass, field

# this is wrong implementation? because we are trying to make default one list to all instances
try:
    @dataclass
    class ClubMember:
        name: str
        guests: set = set() # or make any mutuable object
except Exception as e:
    print(e)

print()

@dataclass
class ClubMember:
    name: str
    guests: list = field(default_factory=list)
print('Correct ClubMember')