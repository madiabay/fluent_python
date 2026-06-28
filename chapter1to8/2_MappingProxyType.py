# НЕИЗМЕНЯЕМЫЕ ОТОБРАЖЕНИЯ (MappingProxyType) - это тип данных в Python, 
# который предоставляет неизменяемый интерфейс к словарю. 
# Он позволяет создавать "просмотр" словаря, который нельзя изменять, но можно читать его содержимое.

from types import MappingProxyType

dct = {'a': 1, 'b': 2, 'c': 3}

d_proxy = MappingProxyType(dct)

print(d_proxy) # Вывод: {'a': 1, 'b': 2, 'c': 3}
print(type(d_proxy)) # Вывод: <class 'mappingproxy'>
print(f"d_proxy['a']\n") # Вывод: 1


# давайте попытаемся добавить новый элемент в d_proxy
try:
    d_proxy['d'] = 4
except TypeError as e:
    print(f"Ошибка: {e}") # Вывод: Ошибка: 'mappingproxy' object does not support item assignment
# давайте попытаемся изменить существующий элемент в d_proxy
try:
    d_proxy['a'] = 10
except TypeError as e:
    print(f"Ошибка: {e}") # Вывод: Ошибка: 'mappingproxy' object does not support item assignment
# давайте попытаемся удалить элемент из d_proxy
try:
    del d_proxy['b']
except TypeError as e:
    print(f"Ошибка: {e}") # Вывод: Ошибка: 'mappingproxy' object does not support item deletion
    print()


# но мы можем изменять исходный словарь dct, и эти изменения будут отражаться в d_proxy
dct['a'] = 10
dct['d'] = 4

print(dct) # Вывод: {'a': 10, 'b': 2, 'c': 3, 'd': 4}
print(d_proxy) # Вывод: {'a': 10, 'b': 2, 'c': 3, 'd': 4}
print(d_proxy['a']) # Вывод: 10
print(d_proxy['d']) # Вывод: 4