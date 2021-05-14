import math

class Figure:
    """A python object that handles operations on numbers with errors"""

    def __init__(self, value, error, percent: bool = False):
        self.value = value

        if percent:
            self.error = error * self.value / 100
        else:
            self.error = error

    # print overload
    def __str__(self):
        return str(self.value) + " +/- " + str(self.error)

    # addition overload
    def __add__(self, other):
        return Figure(self.value + other.value, self.error + other.error)

    # subtraction overload
    def __sub__(self, other):
        return Figure(self.value - other.value, self.error + other.error)

    # negation overload
    def __neg__(self):
        return Figure(-self.value, self.error)

    # multiplication overload 1
    def __mul__(self, other):
        # multiplication between two figures
        if isinstance(other, Figure):
            value = other.value * self.value
            error = value * ((self.error / self.value) + (other.error / other.value))
            return Figure(value, error)

        # scalar multiplication
        elif isinstance(other, float) or isinstance(other, int):
            value = other * self.value
            error = other * self.error
            return Figure(value, error)

        else:
            return float('NaN')

    # multiplication overload 2
    def __rmul__(self, other):
        # multiplication between two figures
        if isinstance(other, Figure):
            value = other.value * self.value
            error = value * ((self.error / self.value) + (other.error / other.value))
            return Figure(value, error)

        # scalar multiplication
        elif isinstance(other, float) or isinstance(other, int):
            value = other * self.value
            error = other * self.error
            return Figure(value, error)

        else:
            return float('NaN')

    # division overload 1
    def __truediv__(self, other):
        # division between two figures
        if isinstance(other, Figure):
            value = self.value / other.value
            error = value * ((self.error / self.value) + (other.error / other.value))
            return Figure(value, error)

        # scalar division
        elif isinstance(other, float) or isinstance(other, int):
            value = self.value / other
            error = self.error / other
            return Figure(value, error)

        else:
            return float('NaN')

    # division overload 2
    def __rtruediv__(self, other):
        # division between two figures
        if isinstance(other, Figure):
            value = other.value / self.value
            error = value * ((self.error / self.value) + (other.error / other.value))
            return Figure(value, error)

        # scalar division
        elif isinstance(other, float) or isinstance(other, int):
            value = other / self.value
            error = other * self.error / math.pow(self.value, 2)
            return Figure(value, error)

        else:
            return float('NaN')

    # power overload
    def __pow__(self, power, modulo=None):
        value = self.value ** power
        error = value * power * self.error / self.value
        return Figure(value, error)

