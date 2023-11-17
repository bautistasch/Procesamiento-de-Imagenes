import tkinter as tk
from typing import Iterable

import numpy as np
from PIL import Image, ImageDraw

# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from ellipse import Ellipse
import math

def generate_ellipse(ellipse: Ellipse):
    c, s = math.cos(ellipse.A), math.sin(ellipse.A)

    coords = []
    for a in np.linspace(0, math.pi * 2, 40):
        x, y = math.cos(a) * ellipse.X, math.sin(a) * ellipse.Y
        coords.append((x, y))

    return [(c*x-s*y+ellipse.Cx, s*x+c*y+ellipse.Cy) for (x,y) in coords]

class EllipseImage(tk.Frame):
    def __init__(self, master=None, size=256, figsize=4, vmin=0, vmax=1, axis='on', title=None):
        super().__init__(master)
        self.image = Image.new("F", (size, size))
        self.image_draw = ImageDraw.Draw(self.image)

        fig = Figure(figsize=(figsize, figsize), dpi=100)
        ax = fig.add_subplot()
        ax.axis(axis)
        image = ax.imshow(np.array(self.image), vmin=vmin, vmax=vmax, cmap='hot')
        if title is not None:
            ax.set_title(title, {'fontsize': 8})
        fig.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()

        canvas.mpl_connect("key_press_event", key_press_handler)

        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.size = size
        self.plt_image = image
        self.canvas = canvas

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

        # required to update canvas and attached toolbar!
        self.canvas.draw()

