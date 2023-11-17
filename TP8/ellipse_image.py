import tkinter as tk
from typing import Iterable

import numpy as np

# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from ellipse import Ellipse



class EllipseImage(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        data = np.zeros((100, 100))

        fig = Figure(figsize=(4, 4), dpi=100)
        ax = fig.add_subplot()
        image = ax.imshow(data)
        # ax.set_xlabel("time [s]")
        # ax.set_ylabel("f(t)")

        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()

        canvas.mpl_connect("key_press_event", key_press_handler)

        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.data = data
        self.image = image
        self.canvas = canvas

    def draw(self, ellipses: Iterable[Ellipse]):
        # retrieve frequency
        f = float(np.round(np.random.uniform() * 10) + 5)

        # update data
        y = 2 * np.sin(2 * np.pi * f * t)
        self.image.set_data(self.data)

        # required to update canvas and attached toolbar!
        self.canvas.draw()

