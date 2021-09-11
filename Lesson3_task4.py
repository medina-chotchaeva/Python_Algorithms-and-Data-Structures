"""
Определить, какое число в массиве встречается чаще всего.
"""
from random import randint

array = [randint(0, 10) for n in range(10)]
print(array)

array_set = set(array)

common = None
q_common = 0
for i in array_set:
    q = array.count(i)
    if q > q_common:
        q_common = q
        common = i

print(common)