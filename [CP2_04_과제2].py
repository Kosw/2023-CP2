class Calculator(object):
    def __init__(self, x):
        self.x = x
    def __str__(self):
        return str(self.x)

    def __add__(self, other):
        return self.x + other.x

    def __sub__(self, other):
        return self.x - other.x

    def __mul__(self, other):
        return self.x * other.x

while True:
    xy = list(map(int, input().split()))
    if xy[0] == 0:
        print("Exit")
        break
    x, y = xy
    calc_x = Calculator(x)
    calc_y = Calculator(y)
    print("x + y =", calc_x + calc_y)
    print("x - y =", calc_x - calc_y)
    print("x * y =", calc_x * calc_y)

