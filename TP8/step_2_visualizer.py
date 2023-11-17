import tkinter as tk
from options_field import OptionsField
from property import Range
from angle_range_form import AngleRangeForm
from numeric_field import NumericField

class Step2Visualizer(tk.Frame):
    on_calculate_listeners = []

    def __init__(self, master=None):
        super().__init__(master)
        
        angle = OptionsField(
            str,
            master=self, 
            label="Ángulo"
        )
        angle.set_options(["asdf", "fdsa"])

        angle.pack()

        self.angle = angle

    def set_options(self, options):
        self.angle.set_options(options)
