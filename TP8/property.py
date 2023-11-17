
from collections import namedtuple
from typing import Generic, NamedTuple, TypeVar

class Range(NamedTuple):
    min: float
    max: float
    step: float

T = TypeVar('T')

class Options(NamedTuple, Generic[T]):
    options: tuple[T]

class RangeProperty(NamedTuple):
    name: str
    label: str
    values: Range
    default: float

class OptionsProperty(NamedTuple, Generic[T]):
    name: str
    label: str
    values: Options[T]
    default: T
