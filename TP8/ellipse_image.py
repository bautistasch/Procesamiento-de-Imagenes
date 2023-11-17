import tkinter as tk
from typing import Iterable

import numpy as np
from PIL import Image, ImageDraw

from image import ImageWidget
from ellipse import Ellipse
import math

def generate_ellipse(ellipse: Ellipse):
    c, s = math.cos(ellipse.A), math.sin(ellipse.A)

    coords = []
    for a in np.linspace(0, math.pi * 2, 40):
        x, y = math.cos(a) * ellipse.X, math.sin(a) * ellipse.Y
        coords.append((x, y))

    return [(c*x-s*y+ellipse.Cx, s*x+c*y+ellipse.Cy) for (x,y) in coords]

class EllipseImage(ImageWidget):
    def __init__(self, size=256, **kwargs):
        super().__init__(**kwargs)
        self.image = Image.new("F", (size, size))
        self.image_draw = ImageDraw.Draw(self.image)

        self.size = size

    def draw(self, ellipses: Iterable[Ellipse]):
        self.image_draw.rectangle((0, 0, self.size, self.size), fill=0)
        scale = self.size / 2
        for ellipse in ellipses:
            self.image_draw.polygon(
                generate_ellipse(
                    Ellipse(
                        I=ellipse.I,
                        A=math.radians(ellipse.A),
                        X=ellipse.X * scale,
                        Y=ellipse.Y * scale,
                        Cx=(ellipse.Cx + 1) * scale,
                        Cy=(-ellipse.Cy + 1) * scale,
                    )
                ), 
                fill=ellipse.I,
                outline=ellipse.I,
                width=0
            )

        self.plt_image.set_data(np.array(self.image))

        super().draw(np.array(self.image))

