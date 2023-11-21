from typing import Any, NamedTuple

class Range(NamedTuple):
    min: float
    max: float
    step: float

class Options(NamedTuple):
    options: tuple

class RangeProperty(NamedTuple):
    name: str
    label: str
    values: Range
    default: float

class OptionsProperty(NamedTuple):
    name: str
    label: str
    values: Options
    default: Any
