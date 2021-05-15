import math
import os
from strings import *


class Figure:
    """A python object that handles operations on numbers with errors"""

    def __init__(self, value, error, percent: bool = False, name=None):

        self.value = value

        if percent:
            self.error = error * self.value / 100
        else:
            self.error = error

        if name is None:
            self.name = str(self.value) + " \\pm  " + str(self.error)
        else:
            self.name = name

    def to_latex(self):
        return self.name

    def display_equation(self):
        webpage = open("equation.html", "w")
        webpage.write(preamble + mathjax_link + wrapper + self.name + close)
        webpage.close()
        os.system("equation.html")

    # print overload
    def __str__(self):
        return str(self.value) + " +/- " + str(self.error)

    # addition overload 1
    def __add__(self, other):
        if isinstance(other, Figure):
            return Figure(self.value + other.value, self.error + other.error, name=self.name + " + " + other.name)
        elif isinstance(other, float) or isinstance(other, int):
            return Figure(self.value + other, self.error, name=self.name + " + " + str(other))

    # addition overload 2
    def __radd__(self, other):
        if isinstance(other, Figure):
            return Figure(self.value + other.value, self.error + other.error, name=other.name + " + " + self.name)
        elif isinstance(other, float) or isinstance(other, int):
            return Figure(self.value + other, self.error, name=str(other) + " + " + self.name)

    # subtraction overload 1
    def __sub__(self, other):
        if isinstance(other, Figure):
            return Figure(self.value - other.value, self.error + other.error, name=self.name + " - " + other.name)
        elif isinstance(other, float) or isinstance(other, int):
            return Figure(self.value - other, self.error, name=self.name + " - " + str(other))

    # subtraction overload 2
    def __rsub__(self, other):
        if isinstance(other, Figure):
            return Figure(other.value - self.value, self.error + other.error, name=other.name + " - " + self.name)
        elif isinstance(other, float) or isinstance(other, int):
            return Figure(other - self.value, self.error, name=str(other) + " - " + self.name)

    # negation overload
    def __neg__(self):
        return Figure(-self.value, self.error, name=" - " + self.name)

    # multiplication overload 1
    def __mul__(self, other):
        # multiplication between two figures
        if isinstance(other, Figure):
            value = other.value * self.value
            error = value * ((self.error / self.value) + (other.error / other.value))
            return Figure(value, error, name=self.name + " \\cdot " + other.name)

        # scalar multiplication
        elif isinstance(other, float) or isinstance(other, int):
            value = other * self.value
            error = other * self.error
            return Figure(value, error, name=self.name + " \\cdot " + str(other))

        else:
            return float('NaN')

    # multiplication overload 2
    def __rmul__(self, other):
        # multiplication between two figures
        if isinstance(other, Figure):
            value = other.value * self.value
            error = value * ((self.error / self.value) + (other.error / other.value))
            return Figure(value, error, name=other.name + " \\cdot " + self.name)

        # scalar multiplication
        elif isinstance(other, float) or isinstance(other, int):
            value = other * self.value
            error = other * self.error
            return Figure(value, error, name=str(other) + " \\cdot " + self.name)

        else:
            return float('NaN')

    # division overload 1
    def __truediv__(self, other):
        # division between two figures
        if isinstance(other, Figure):
            value = self.value / other.value
            error = value * ((self.error / self.value) + (other.error / other.value))
            return Figure(value, error, name="\\frac{" + self.name + "}{" + other.name + "}")

        # scalar division
        elif isinstance(other, float) or isinstance(other, int):
            value = self.value / other
            error = self.error / other
            return Figure(value, error, name="\\frac{" + self.name + "}{" + str(other) + "}")

        else:
            return float('NaN')

    # division overload 2
    def __rtruediv__(self, other):
        # division between two figures
        if isinstance(other, Figure):
            value = other.value / self.value
            error = value * ((self.error / self.value) + (other.error / other.value))
            return Figure(value, error, name="\\frac{" + other.name + "}{" + self.name + "}")

        # scalar division
        elif isinstance(other, float) or isinstance(other, int):
            value = other / self.value
            error = other * self.error / math.pow(self.value, 2)
            return Figure(value, error, name="\\frac{" + str(other) + "}{" + self.name + "}")

        else:
            return float('NaN')

    # power overload
    def __pow__(self, power, modulo=None):
        value = self.value ** power
        error = value * power * self.error / self.value
        return Figure(value, error, name=self.name + "^{" + str(power) + "}")
