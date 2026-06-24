from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
almaty = City('Almaty', 'KZ', 2_000_000, (35.35, 70.35))

print(almaty)

print(almaty.population)
print(almaty.coordinates)
print(almaty[1])

print()

print(City._fields)
print(type(City._fields))

Coordinate = namedtuple('Coordinate', 'lat lon')
delhi_data = ('Delhi NCR', 'IN', 21.9999, Coordinate(29.23, 23.11))
delhi = City._make(delhi_data)
print(delhi)
print(type(delhi))
print(delhi._asdict())

print()

import json
json_dump = json.dumps(delhi._asdict())
print(json_dump)
