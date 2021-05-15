from figure import Figure
import math


def ln(figure: Figure):
    value = math.log(figure.value)
    error = figure.error / figure.value
    return Figure(value, error, name="\\ln \\left( " + figure.name + " \\right)")


def log(figure: Figure, base=10):
    value = math.log(figure.value) / math.log(base)
    error = figure.error / (figure.value * math.log(base))
    return Figure(value, error, name="\\log_" + str(base) + " \\left( " + figure.name + " \\right)")


def antiln(figure: Figure):
    value = math.exp(figure.value)
    error = math.exp(figure.value) * figure.error
    return Figure(value, error, name="\\exp \\left( " + figure.name + " \\right)")


def antilog(figure: Figure, base=10):
    value = math.pow(base, figure.value)
    error = math.pow(base, figure.value) * math.log(base) * figure.error
    return Figure(value, error, name=str(base) + "^{" + figure.name + "}")
