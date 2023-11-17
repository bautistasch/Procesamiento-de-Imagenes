import tkinter as tk
from tkinter import ttk
from ellipse import Ellipse, properties
from ellipse_image import EllipseImage
from ellipse_form import EllipseForm
from ellipse_table import EllipseTable


class InputPanel(tk.Frame):
    def __init__(self, master=None) -> None:
        super().__init__(master)

        table = EllipseTable(self)
        form = EllipseForm(self)

        def add_ellipse():
            table.add_item(form.get_ellipse())

        buttons = tk.Frame(self)
        button_insert = tk.Button(buttons, text="Agregar", command=add_ellipse)
        button_remove = tk.Button(buttons, text="Eliminar", command=table.delete_selected)
        button_insert.pack()
        button_remove.pack(side=tk.RIGHT)

        image = EllipseImage(self)

        table.grid(row=0, rowspan=3, column=0)
        image.grid(row=0, column=1)
        form.grid(row=1, column=1)
        buttons.grid(row=2, column=1)
