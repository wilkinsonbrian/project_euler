class Fraction:

    def __init__(self, num, den):
        factor = self.reduce(num, den)
        self.numerator = num / factor
        self.denominator = den / factor

    def reduce(self, x, y):
        while(y):
            x, y = y, x % y
        return x

    def add(self, f2):
        num = self.numerator * f2.denominator + f2.numerator * self.denominator
        den = self.denominator * f2.denominator
        return Fraction(num, den)

    def divide(self, f2):
        num = self.numerator * f2.denominator
        den = self.denominator * f2.numerator
        return Fraction(num, den)

    def multiply(self, f2):
        num = self.numerator * f2.numerator
        den = self.denominator * f2.denominator
        return Fraction(num, den)


