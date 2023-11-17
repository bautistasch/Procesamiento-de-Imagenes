import tkinter as tk

import numpy as np

# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class ImageWidget(tk.Frame):
    def __init__(self, master=None, figsize=4, vmin=0, vmax=1, axis='on', title=None):
        super().__init__(master)
        fig = Figure(figsize=(figsize, figsize), dpi=100)
        ax = fig.add_subplot()
        ax.axis(axis)
        image = ax.imshow(np.zeros((10, 10), dtype=np.float32), vmin=vmin, vmax=vmax, cmap='hot')
        if title is not None:
            ax.set_title(title, {'fontsize': 8})
        fig.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()

        canvas.mpl_connect("key_press_event", key_press_handler)

        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.plt_image = image
        self.canvas = canvas

    def draw(self, image: np.ndarray):
        self.plt_image.set_data(image)
        self.canvas.draw()

