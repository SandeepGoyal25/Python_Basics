# list1 = ['N1:sandy', 'N2:babbu', 'N3:akhi', 'N4:pandu']
# print(list1(N1))
from unittest import result


def concatenate(list):
    result = ''
    for element in list:
        result += str(element)
    return result

print(concatenate([1, 7, 90, 36, 0, 0]))