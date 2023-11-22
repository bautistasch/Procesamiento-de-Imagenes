import tkinter as tk
from typing import Iterable
from image import ImageWidget
from options_field import OptionsField
from property import Range
from angle_range_form import AngleRangeForm
from numeric_field import NumericField
import numpy as np
import matplotlib.pyplot as plt

class Step2Visualizer(tk.Frame):
    images = []
    floats_as_strings = []

    def __init__(self, master=None):
        super().__init__(master)
        
        angle = OptionsField(
            str,
            master=self, 
            label="Ángulo"
        )
        angle.set_on_change(lambda v:self.show_plot(v))
        image_widget = ImageWidget(self,
            xlabel="Projection angle (deg)",
            ylabel="Projection position (pixels)"
        )

        image_widget.pack()
        angle.pack()

        self.image_widget = image_widget
        self.angle = angle

    def show_plot(self, angle):
        y = self.images[:, self.floats_as_strings.index(angle)]
        plt.plot(np.linspace(-180, 180, len(y)), y)
        plt.show(block=False)

    def set_options(self, options: list[float], images: list[np.ndarray]):
        self.floats_as_strings: list[str | None] = list(map(str, options))

        self.images = images
        self.image_widget.draw(
            images, 
            vmin=0, 
            vmax=np.max(images), 
            extent=(np.min(options), np.max(options), -180, 180)
        )
        self.angle.set_options(self.floats_as_strings)

