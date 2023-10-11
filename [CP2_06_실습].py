lst = [1, 2, 3, 4, 5]
lst_1 = [2*x for x in lst]
print("[2*x for x in lst]")
print(lst_1)
lst_2 = [2*x for x in lst if x > 3]
print("[2*x for x in lst if x > 3]")
print(lst_2)
lst_3 = [2*x for x in lst if x <= 2]
print("[2*x for x in lst if x <= 2]")
print(lst_3)
lst_4 = [[x, x**2] for x in lst]
print("[[x, x**2] for x in lst]")
print(lst_4)

a = (x*x for x in range(5))
for i in range(5):
    print(next(a))


def integers():
    i = 1
    while True:
        yield i
        i += 1

def take(n, seq):
    seq = iter(seq)
    result = []
    try:
        for i in range(n):
            result.append(next(seq))
    except StopIteration:
        pass
    return result

pyt = ((x, y, z)
       for z in integers()
       for y in range(1, z)
       for x in range(1, y) if x*x + y*y == z*z)
print(take(7, pyt))

def func():
    lst = [1, 2, 3, 4, 5]
    for i in lst:
        yield i

f = func()
try:
    for i in range(5):
        print(next(f))
except StopIteration:
    print("Error StopIteration")
else:
    print("Printing Success")
finally:
    print("Exit")

def func(data):
    assert isinstance(data, list)
    print("Print data list")
    print(data)

print("Input List")
lst = [1, 2, 3, 4, 5]
func(lst)
print("Input Dummy tuple")
dummy = (1, 2, 3, 4, 5)
func(dummy)

