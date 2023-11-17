import tkinter as tk
from angle_range_form import AngleRangeForm
from numeric_field import NumericField

class Step2Form(tk.Frame):
    on_calculate_listeners = []

    def __init__(self, master=None):
        super().__init__(master)
        
        angle_range_form = AngleRangeForm(self)
        angle_range_form.pack()
        self.angle_range_form = angle_range_form

    def get_params(self):
        return self.angle_range_form.get_angle_range()

    def add_on_calculate_listener(self, callback):
        self.on_calculate_listeners.append(callback)

    def call_on_calculate(self, ellipse):
        for callback in self.on_calculate_listeners:
            callback(ellipse)

    def on_change(self, *_):
        self.call_on_calculate(self.get_params())
