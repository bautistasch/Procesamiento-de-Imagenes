import tkinter as tk
from options_field import OptionsField
from image import ImageWidget
from angle_range_form import AngleRangeForm
from step_2 import Step2
import numpy as np
import implementation

interpolations = ['Nearest Neighbor']
filters = ['ramp', 'shepp-logan', 'cosine', 'hamming', 'hann']

class Step3(tk.Frame):
    on_calculate_listeners = []

    def __init__(self, step_2: Step2, master=None):
        super().__init__(master)
        
        angle_range_form = AngleRangeForm(self, vars=step_2.form.angle_range_form.get_vars())
        interpolation = OptionsField(str, master=self, label='Interpolación', value='')
        interpolation.set_options(interpolations)
        filter = OptionsField(str, master=self, label='Filtro', value='')
        filter.set_options(filters)
        calculate_button = tk.Button(self, command=self.on_calculate, text="Calcular")
        image = ImageWidget(self)

        angle_range_form.pack()
        interpolation.pack()
        filter.pack()
        calculate_button.pack()
        image.pack()

        self.angle_range_form = angle_range_form
        self.calculate_button = calculate_button
        self.step_2 = step_2
        self.interpolation = interpolation
        self.filter = filter
        self.image = image
    
    def on_calculate(self):
        if self.step_2.results is not None:
            radon = self.step_2.results

            angles = self.angle_range_form.get_angle_range()
            reconstructed = implementation.inverse_radon(radon, np.arange(angles.min, angles.max, angles.step), self.interpolation.get_value(), self.filter.get_value(), 256)
            self.image.draw(reconstructed)
