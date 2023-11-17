
import tkinter as tk
from collections import namedtuple
from ellipse import Ellipse, properties, property_names


class EllipseForm(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        
        entries = []
        property_entries = {}
        for i, (property, name) in enumerate(zip(properties, property_names)):
            label = tk.Label(self, text=name)
            label.grid(row=i, column=0)
            var = tk.StringVar()
            var.set("0.0")
            entry = tk.Entry(self, textvariable=var)
            entry.grid(row=i, column=1)
            entries.append((label, entry))
            property_entries[property] = entry
        self.property_entries = property_entries

    def get_ellipse(self) -> Ellipse:
        return Ellipse(**{p:float(v.get()) for p, v in self.property_entries.items()})

