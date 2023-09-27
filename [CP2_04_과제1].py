class Fraction(object):
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):

        if self.numerator % self.denominator == 0:
            return str(int(self.numerator / self.denominator))

        else:
            return str(self.numerator) + "/" + str(self.denominator)


while True:
    f = list(map(int, input().split()))
    if f[0] == 0:
        print("Exit")
        break
    else:
        print(Fraction(f[0], f[1]))
