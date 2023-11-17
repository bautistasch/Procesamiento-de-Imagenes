import tkinter as tk
from angle_range_form import AngleRangeForm
from step_2 import Step2
import numpy as np

class Step3(tk.Frame):
    on_calculate_listeners = []

    def __init__(self, step_2: Step2, master=None):
        super().__init__(master)
        
        angle_range_form = AngleRangeForm(self, vars=step_2.form.angle_range_form.get_vars())
        # calculate_button = tk.Button(self, command=self.on_calculate, text="Calcular")

        angle_range_form.pack()
        # calculate_button.pack()

        self.angle_range_form = angle_range_form
        # self.calculate_button = calculate_button
