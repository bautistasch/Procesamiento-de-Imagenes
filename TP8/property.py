
from collections import namedtuple
from typing import NamedTuple

class Range(NamedTuple):
    min: float
    max: float
    increment: float

class Property(NamedTuple):
    name: str
    label: str
    values: Range
    default: float
