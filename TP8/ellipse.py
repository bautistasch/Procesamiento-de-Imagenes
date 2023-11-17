
from collections import namedtuple

from property import Property, Range

properties = ("I", "A", "X", "Y", "Cx", "Cy")

Ellipse = namedtuple('Ellipse', properties)
default_ellipse = Ellipse(I=.6, A=0, Cx=0.2, Cy=0.5, X=.3, Y=.4)

properties = (
    Property("I", "Intensidad", Range(0, 1, 0.05), default_ellipse.I),
    Property("A", "Inclinación", Range(-360, 360, 15), default_ellipse.A), 
    Property("X", "Semi-eje X", Range(-2, 2, 0.1), default_ellipse.X), 
    Property("Y", "Semi-eje Y", Range(-2, 2, 0.1), default_ellipse.Y), 
    Property("Cx", "Centro X", Range(-2, 2, 0.1), default_ellipse.Cx), 
    Property("Cy", "Centro Y", Range(-2, 2, 0.1), default_ellipse.Cy)
)

