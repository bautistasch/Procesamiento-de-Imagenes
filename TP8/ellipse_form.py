
import tkinter as tk
from ellipse import Ellipse, properties, property_names

default_ellipse = Ellipse(I=.3, A=90, Cx=-.4, Cy=0, X=.2, Y=.4)
default_ellipse = Ellipse(I=.6, A=0, Cx=0.2, Cy=0.5, X=.3, Y=.4)

class EllipseForm(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        
        entries = []
        property_entries = {}
        for i, (property, name) in enumerate(zip(properties, property_names)):
            label = tk.Label(self, text=name)
            label.grid(row=i, column=0)
            var = tk.StringVar()
            var.set(str(default_ellipse[i]))
            entry = tk.Entry(self, textvariable=var)
            entry.grid(row=i, column=1)
            entries.append((label, entry))
            property_entries[property] = entry
        self.property_entries = property_entries

    def get_ellipse(self) -> Ellipse:
        return Ellipse(**{p:float(v.get()) for p, v in self.property_entries.items()})

