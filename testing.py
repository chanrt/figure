from figure import Figure
from trigs import *
from logs import *

a = Figure(5, 0.1, name="a")
b = Figure(10, 1, name="b")
c = Figure(1, 0.1, name="c")
d = Figure(60, 2, name="d")
e = Figure(16, 1)

result = (a ** 2 / b ** 3) - c + sine(d, False) - log(e, base=2)

print(result)
print(result.to_latex())
