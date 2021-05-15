from figure import Figure
import math


def sine(figure: Figure, radian_mode: bool = True):
    if radian_mode:
        value = math.sin(figure.value)
        error = math.cos(figure.value) * figure.error
        return Figure(value, error, name="\\sin \\left( " + figure.name + " \\right)")

    else:
        value = math.sin(_to_radian(figure.value))
        error = math.cos(_to_radian(figure.value)) * _to_radian(figure.error)
        return Figure(value, error, name="\\sin \\left( " + figure.name + " \\right)")


def cosine(figure: Figure, radian_mode: bool = True):
    if radian_mode:
        value = math.cos(figure.value)
        error = math.sin(figure.value) * figure.error
        return Figure(value, error, name="\\cos \\left( " + figure.name + " \\right)")

    else:
        value = math.cos(_to_radian(figure.value))
        error = math.sin(_to_radian(figure.value)) * _to_radian(figure.error)
        return Figure(value, error, name="\\cos \\left( " + figure.name + " \\right)")


def tangent(figure: Figure, radian_mode: bool = True):
    if radian_mode:
        value = math.tan(figure.value)
        error = figure.error / math.pow(math.cos(figure.value), 2)
        return Figure(value, error, name="\\tan \\left( " + figure.name + " \\right)")

    else:
        value = math.tan(_to_radian(figure.value))
        error = _to_radian(figure.error) / math.pow(math.cos(_to_radian(figure.value)), 2)
        return Figure(value, error, name="\\tan \\left( " + figure.name + " \\right)")


def asine(figure: Figure, radian_mode: bool = True):
    if radian_mode:
        value = math.asin(figure.value)
        error = figure.error / math.sqrt(1 - math.pow(figure.value, 2))
        return Figure(value, error, name="\\asin \\left( " + figure.name + " \\right)")

    else:
        value = _to_degree(math.asin(figure.value))
        error = _to_degree(figure.error / math.sqrt(1 - math.pow(figure.value, 2)))
        return Figure(value, error, name="\\asin \\left( " + figure.name + " \\right)")


def acosine(figure: Figure, radian_mode: bool = True):
    if radian_mode:
        value = math.acos(figure.value)
        error = figure.error / math.sqrt(1 - math.pow(figure.value, 2))
        return Figure(value, error, name="\\acos \\left( " + figure.name + " \\right)")

    else:
        value = _to_degree(math.acos(figure.value))
        error = _to_degree(figure.error / math.sqrt(1 - math.pow(figure.value, 2)))
        return Figure(value, error, name="\\acos \\left( " + figure.name + " \\right)")


def atangent(figure: Figure, radian_mode: bool = True):
    if radian_mode:
        value = math.atan(figure.value)
        error = figure.error / (1 + math.pow(figure.value, 2))
        return Figure(value, error, name="\\atan \\left( " + figure.name + " \\right)")

    else:
        value = _to_degree(math.atan(figure.value))
        error = _to_degree(figure.error / (1 + math.pow(figure.value, 2)))
        return Figure(value, error, name="\\atan \\left( " + figure.name + " \\right)")


def _to_radian(degree):
    return math.pi * degree / 180


def _to_degree(radian):
    return 180 * radian / math.pi