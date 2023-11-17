
import tkinter as tk
from ellipse import Ellipse, properties, property_names

default_ellipse = Ellipse(I=.3, A=90, Cx=-.4, Cy=0, X=.2, Y=.4)
default_ellipse = Ellipse(I=.6, A=0, Cx=0.2, Cy=0.5, X=.3, Y=.4)

class EllipseForm(tk.Frame):
    on_change_listeners = []

    def __init__(self, master=None):
        super().__init__(master)
        
        entries = []
        property_entries = {}
        for i, (property, name) in enumerate(zip(properties, property_names)):
            label = tk.Label(self, text=name)
            label.grid(row=i, column=0)
            var = tk.StringVar()
            var.set(str(default_ellipse[i]))
            var.trace_add("write", callback=lambda var,index,mode:self.on_change())
            entry = tk.Entry(self, textvariable=var)
            entry.bind('<FocusOut>', self.on_unfocused)
            entry.bind('<FocusIn>', self.on_focused)
            entry.grid(row=i, column=1)
            entries.append((label, entry, var))
            property_entries[property] = entry
        self.property_entries = property_entries
        self.entries = entries

        self.on_change()

    def get_ellipse(self) -> Ellipse:
        return Ellipse(**{p:float(v.get()) for p, v in self.property_entries.items()})

    def add_on_change_listener(self, callback):
        self.on_change_listeners.append(callback)

    def call_on_change(self, ellipse):
        for callback in self.on_change_listeners:
            callback(ellipse)

    def on_change(self, *_):
        self.call_on_change(self.get_ellipse())

    def on_unfocused(self, *_):
        self.call_on_change(None)

    def on_focused(self, *_):
        self.call_on_change(self.get_ellipse())
