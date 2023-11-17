from collections import namedtuple
import tkinter as tk
from property import Property, Range
from numeric_field import NumericField

properties = (
    Property("from", "Desde", Range(-360, 360, 15), 0),
    Property("step", "Paso", Range(-360, 360, 5), 10),
    Property("to", "Hasta", Range(-360, 360, 15), 180),
)

class AngleRangeForm(tk.Frame):
    on_change_listener = []

    def __init__(self, master=None):
        super().__init__(master)
        property_entries = {}
        for i, prop in enumerate(properties):
            field = NumericField(self, range=prop.values, label=prop.name, value=prop.default)
            field.set_on_change(lambda v:self.on_change())
            field.grid(row=i)
            property_entries[property] = field

    def get_angle_range(self):
        return self.property_entries
    
