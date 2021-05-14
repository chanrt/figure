from figure import Figure
import math


def sine(figure: Figure, radian_mode: bool = True):
    if radian_mode:
        value = math.sin(figure.value)
        error = math.cos(figure.value) * figure.error
        return Figure(value, error)

    else:
        value = math.sin(_to_radian(figure.value))
        error = math.cos(_to_radian(figure.value)) * _to_radian(figure.error)
        return Figure(value, error)


def cosine(figure: Figure, radian_mode: bool = True):
    if radian_mode:
        value = math.cos(figure.value)
        error = math.sin(figure.value) * figure.error
        return Figure(value, error)

    else:
        value = math.cos(_to_radian(figure.value))
        error = math.sin(_to_radian(figure.value)) * _to_radian(figure.error)
        return Figure(value, error)


def tangent(figure: Figure, radian_mode: bool = True):
    if radian_mode:
        value = math.tan(figure.value)
        error = figure.error / math.pow(math.cos(figure.value), 2)
        return Figure(value, error)

    else:
        value = math.tan(_to_radian(figure.value))
        error = _to_radian(figure.error) / math.pow(math.cos(_to_radian(figure.value)), 2)
        return Figure(value, error)


def asine(figure: Figure, radian_mode: bool = True):
    if radian_mode:
        value = math.asin(figure.value)
        error = figure.error / math.sqrt(1 - math.pow(figure.value, 2))
        return Figure(value, error)

    else:
        value = _to_degree(math.asin(figure.value))
        error = _to_degree(figure.error / math.sqrt(1 - math.pow(figure.value, 2)))
        return Figure(value, error)


def acosine(figure: Figure, radian_mode: bool = True):
    if radian_mode:
        value = math.acos(figure.value)
        error = figure.error / math.sqrt(1 - math.pow(figure.value, 2))
        return Figure(value, error)

    else:
        value = _to_degree(math.acos(figure.value))
        error = _to_degree(figure.error / math.sqrt(1 - math.pow(figure.value, 2)))
        return Figure(value, error)


def atangent(figure: Figure, radian_mode: bool = True):
    if radian_mode:
        value = math.atan(figure.value)
        error = figure.error / (1 + math.pow(figure.value, 2))
        return Figure(value, error)

    else:
        value = _to_degree(math.atan(figure.value))
        error = _to_degree(figure.error / (1 + math.pow(figure.value, 2)))
        return Figure(value, error)


def _to_radian(degree):
    return math.pi * degree / 180


def _to_degree(radian):
    return 180 * radian / math.pi