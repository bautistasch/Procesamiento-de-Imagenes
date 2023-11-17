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

        input_frame = tk.Frame(self)
        form = EllipseForm(input_frame)
        preview = EllipseImage(input_frame, size=30, figsize=1, axis='off', title='Previsualización')

        props = {"padx": 5.0, "pady": 5.0}
        form.grid(row=0, column=0, **props)
        preview.grid(row=0, column=1, **props)

        def add_ellipse():
            table.add_item(form.get_ellipse())

        buttons = tk.Frame(self)
        button_insert = tk.Button(buttons, text="Agregar", command=add_ellipse)
        button_remove = tk.Button(buttons, text="Eliminar", command=table.delete_selected)
        button_insert.pack(side=tk.LEFT)
        button_remove.pack(side=tk.RIGHT)

        image = EllipseImage(self)

        def draw_ellipses(e):
            image.draw(e)
        table.add_change_listener(draw_ellipses)
        form.add_on_change_listener(lambda e:print(e))
        def draw_preview(f):
            # image.draw(ellipses + ([f] if f is not None else []))
            if f is not None:
                preview.draw([f])
        form.add_on_change_listener(draw_preview)
        form.on_change()

        props = {"padx": 20.0, "pady": 5.0}
        table.grid(row=0, rowspan=4, column=0, **props)
        image.grid(row=0, column=1, **props)
        input_frame.grid(row=1, column=1, **props)
        buttons.grid(row=2, column=1, **props)
