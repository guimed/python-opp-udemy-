# without @staticmethod

class Fraction:
    def __init__(self, nr, dr=1):
        self.nr = nr
        self.dr = dr
        if self.dr < 0:
            self.nr *= -1
            self.dr *= -1
            
    def show(self):
        print(str(self.nr) + '/' + str(self.dr))

    def multiply(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return Fraction(self.nr * other.nr, self.dr * other.dr)
        
    def add(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return Fraction(self.nr * other.dr + other.nr * self.dr, self.dr * other.dr)

    def hcf(self):
        x = abs(self.nr)
        y = abs(self.dr)
        smaller = y if x > y else x
        s = smaller
        while s>0:
            if x %s == 0 and y % s == 0:
                break
            s -= 1
        return s

    def _reduce(self):
        div = self.hcf()
        print('reduced fraction', (str(self.nr / div)) + '/' + (str(self.dr / div)))

