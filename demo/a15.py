# encoding:UTF-8

import array

a = array.array('i', [1, 2, 3, 4, 5])
b = array.array('i', [5, 6, 7, 8, 9])
print(a[2])
print(b[2])

a.pop(2)
print(a)
a.insert([1, 1, 1])
#a.append([1, 1, 1])
print(a)
