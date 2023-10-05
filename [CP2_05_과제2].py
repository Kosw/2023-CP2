from functools import reduce


def reverse(lst):
    for i in range(len(lst) - 1, -1, -1):
        yield lst[i]


my_input = int(input())
lst = list(range(my_input))
rev_lst = []
for i in reverse(lst):
    rev_lst.append(i)

filter_lst = list(filter(lambda x: x % 2 == 0, rev_lst))
map_list = list(map(lambda x: x ** 2, filter_lst))
result = reduce(lambda x, y: x + y, map_list)
print(result)
