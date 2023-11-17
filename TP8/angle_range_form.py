from collections import namedtuple
import tkinter as tk
from property import RangeProperty, Range
from numeric_field import NumericField

properties = (
    RangeProperty("from", "Desde", Range(-360, 360, 15), 0),
    RangeProperty("step", "Paso", Range(-360, 360, 5), 10),
    RangeProperty("to", "Hasta", Range(-360, 360, 15), 180),
)

class AngleRangeForm(tk.Frame):
    on_change_listener = []

    def __init__(self, master=None, vars=None):
        super().__init__(master)
        property_entries = {}
        if vars is None: vars = [None, None, None]
        for i, (prop, var) in enumerate(zip(properties, vars)):
            field = NumericField(self, range=prop.values, label=prop.name, value=prop.default, var=var)
            field.grid(row=i)
            property_entries[prop.name] = field

        self.property_entries = property_entries

    def get_angle_range(self) -> Range:
        min = self.property_entries["from"]
        max = self.property_entries["to"]
        step = self.property_entries["step"]
        return Range(min.get_value(), max.get_value(), step.get_value())
    
    def get_vars(self):
        min = self.property_entries["from"]
        step = self.property_entries["step"]
        max = self.property_entries["to"]
        return (min.var, step.var, max.var)
