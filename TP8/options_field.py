import tkinter as tk
import tkinter.ttk as ttk
from typing import Callable, Generic, Optional, TypeVar, Union
from property import Options, Range

T = TypeVar('T')

class OptionsField(tk.Frame, Generic[T]):
    def __init__(
            self, 
            convert_to_t: Callable[[str], T],
            master=None, 
            value: T = None, 
            label=None,
        ):
        super().__init__(master)

        self.convert_to_t=convert_to_t

        var = tk.StringVar()
        var.set(str(value))

        self.var = var
        
        entry = ttk.Combobox(self, state='readonly', textvariable=var)
        if label is not None:
            label_widget = tk.Label(self, text=label)
            label_widget.grid(column=0, row=0)
            entry.grid(column=1, row=0)
        else:
            label_widget = None
            entry.grid(column=0, row=0, columnspan=2)

        self.label = label_widget
        self.entry = entry

    def set_options(self, options: list[T], default = 0):
        self.options = {
            str(v): v
            for v in options
        }

        self.entry['values'] = list(self.options.keys())
        self.var.set(str(options[default]))

    def set_on_change(self, on_change: Optional[Callable[[T], None]]=None):
        if on_change is not None:
            self.on_change = on_change
        else:
            self.on_change = lambda _:None

        self.var.trace_add("write", callback=lambda *_:self.on_change(self.convert_to_t(self.var.get())))

    def get_value(self):
        return float(self.var.get())
    
