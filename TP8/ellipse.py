
from collections import namedtuple

from property import RangeProperty, Range

properties = ("I", "A", "X", "Y", "Cx", "Cy")

Ellipse = namedtuple('Ellipse', properties)
default_ellipse = Ellipse(I=.6, A=0, Cx=0.2, Cy=0.5, X=.3, Y=.4)

properties = (
    RangeProperty("I", "Intensidad", Range(0, 1, 0.05), default_ellipse.I),
    RangeProperty("A", "Inclinación", Range(-360, 360, 15), default_ellipse.A), 
    RangeProperty("X", "Semi-eje X", Range(-2, 2, 0.1), default_ellipse.X), 
    RangeProperty("Y", "Semi-eje Y", Range(-2, 2, 0.1), default_ellipse.Y), 
    RangeProperty("Cx", "Centro X", Range(-2, 2, 0.1), default_ellipse.Cx), 
    RangeProperty("Cy", "Centro Y", Range(-2, 2, 0.1), default_ellipse.Cy)
)

