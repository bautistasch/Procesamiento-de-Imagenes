import tkinter as tk
from typing import Callable, Optional, Union
from property import Options, Range


class NumericField(tk.Frame):
    def __init__(
            self, 
            master=None, 
            range=Range(0, 1, 0.1), 
            value:float=0, 
            label=None,
            var=None
        ):
        super().__init__(master)

        if var is None:
            var = tk.StringVar()
            var.set(str(value))

        self.var = var
        
        entry = tk.Spinbox(self, textvariable=var, increment=range.step, format="%.2f", from_=range.min, to=range.max)
        if label is not None:
            label_widget = tk.Label(self, text=label)
            label_widget.grid(column=0, row=0)
            entry.grid(column=1, row=0)
        else:
            label_widget = None
            entry.grid(column=0, row=0, columnspan=2)

        self.label = label_widget
        self.entry = entry

    def set_on_change(self, on_change: Optional[Callable[[float], None]]=None):
        if on_change is not None:
            self.on_change = on_change
        else:
            self.on_change = lambda _:None

        self.var.trace_add("write", callback=lambda *_:self.on_change(float(self.var.get())))

    def get_value(self):
        return float(self.var.get())
    
