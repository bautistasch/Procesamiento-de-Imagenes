
import tkinter as tk
from tkinter import ttk
from ellipse import Ellipse, properties


class EllipseTable(tk.Frame):
    ellipses = []
    change_callbacks = []

    def __init__(self, master=None) -> None:
        super().__init__(master)
        # self.label = tkinter.Label(self, text="AAAAAAAA")
        tree= ttk.Treeview(self, columns=properties, show='headings')
        for i, column in enumerate(properties):
            tree.column(f"#{i+1}", anchor=tk.CENTER)
            tree.heading(f"#{i+1}", text=column)
        tree.pack(fill=tk.Y, expand=True)

        tree.bind('<ButtonRelease-1>', self.select_item)

        self.tree = tree

    def select_item(self, item):
        self.selectedItem = self.tree.focus()
    
    def emit_changed(self):
        self.ellipses = list(Ellipse(*row['values']) for row in map(self.tree.item, self.tree.get_children()))
        for callback in self.change_callbacks:
            callback(self.ellipses)

    def delete_selected(self):
        self.tree.delete(self.selectedItem)
        self.emit_changed()

    def add_item(self, ellipse: Ellipse):
        self.tree.insert("", tk.END, values=ellipse)
        self.emit_changed()

    def add_change_listener(self, callback):
        self.change_callbacks.append(callback)

