
from collections import namedtuple


properties = ("I", "A", "X", "Y", "Cx", "Cy")
property_names = ("Intensidad", "Inclinación", "Semi-eje X", "Semi-eje Y", "Centro X", "Centro Y")
Ellipse = namedtuple('Ellipse', properties)

