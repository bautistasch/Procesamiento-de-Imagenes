
import tkinter as tk
from ellipse import Ellipse, properties
from numeric_field import NumericField

default_ellipse = Ellipse(I=.3, A=90, Cx=-.4, Cy=0, X=.2, Y=.4)
default_ellipse = Ellipse(I=.6, A=0, Cx=0.2, Cy=0.5, X=.3, Y=.4)

class EllipseForm(tk.Frame):
    on_change_listeners = []

    def __init__(self, master=None):
        super().__init__(master)
        
        property_entries = {}
        for i, prop in enumerate(properties):
            field = NumericField(self, range=prop.values, label=prop.label, value=default_ellipse[i])
            field.set_on_change(lambda v:self.on_change())
            field.grid(row=i)
            property_entries[prop.name] = field

        self.property_entries = property_entries

    def get_ellipse(self) -> Ellipse:
        return Ellipse(**{p:v.get_value() for p, v in self.property_entries.items()})

    def add_on_change_listener(self, callback):
        self.on_change_listeners.append(callback)

    def call_on_change(self, ellipse):
        for callback in self.on_change_listeners:
            callback(ellipse)

    def on_change(self, *_):
        self.call_on_change(self.get_ellipse())
