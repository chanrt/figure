from figure import Figure
import math


def ln(figure: Figure):
    value = math.log(figure.value)
    error = figure.error / figure.value
    return Figure(value, error)


def log(figure: Figure, base=10):
    value = math.log(figure.value) / math.log(base)
    error = figure.error / (figure.value * math.log(base))
    return Figure(value, error)


def antiln(figure: Figure):
    value = math.exp(figure.value)
    error = math.exp(figure.value) * figure.error
    return Figure(value, error)


def antilog(figure: Figure, base=10):
    value = math.pow(base, figure.value)
    error = math.pow(base, figure.value) * math.log(base) * figure.error
    return Figure(value, error)
