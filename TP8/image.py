import tkinter as tk

import numpy as np

# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class ImageWidget(tk.Frame):
    def __init__(self, master=None, figsize=4, vmin=0, vmax=1, axis='on', title=None, xlabel=None, ylabel=None, colorbar=True):
        super().__init__(master)
        fig = Figure(figsize=(figsize, figsize), dpi=100)
        ax = fig.add_subplot()
        ax.axis(axis)
        image = ax.imshow(np.zeros((10, 10), dtype=np.float32), vmin=vmin, vmax=vmax, cmap='hot', interpolation='none', aspect='auto')
        if title is not None:
            ax.set_title(title, {'fontsize': 8})
        if colorbar:
            fig.colorbar(image, ax=ax)
        if xlabel is not None:
            ax.set_xlabel(xlabel)
        if ylabel is not None:
            ax.set_ylabel(ylabel)
        fig.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()

        canvas.mpl_connect("key_press_event", key_press_handler)

        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.plt_image = image
        self.ax = ax
        self.canvas = canvas
        self.image = None

    def draw(self, image: np.ndarray, vmin=None, vmax=None, extent=None):
        if vmax is not None and vmin is not None:
            self.plt_image.set_clim(vmin=vmin, vmax=vmax)
        self.plt_image.set_data(image)
        if extent is not None:
            self.plt_image.set_extent(extent)
        self.image = image
        self.canvas.draw()

    def get_image(self):
        return self.image
