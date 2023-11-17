
from collections import namedtuple

Range = namedtuple('Range', ('min', 'max', 'increment'))

properties = ("I", "A", "X", "Y", "Cx", "Cy")
property_names = ("Intensidad", "Inclinación", "Semi-eje X", "Semi-eje Y", "Centro X", "Centro Y")
property_ranges = (Range(0, 1, 0.05), Range(-360, 360, 15), Range(-2, 2, 0.1), Range(-2, 2, 0.1), Range(-2, 2, 0.1), Range(-2, 2, 0.1))
Ellipse = namedtuple('Ellipse', properties)

