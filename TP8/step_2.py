import tkinter as tk
from step_2_form import Step2Form
from step_2_visualizer import Step2Visualizer
import numpy as np
import implementation

class Step2(tk.Frame):
    on_calculate_listeners = []

    def __init__(self, image_getter, master=None):
        super().__init__(master)
        
        step2 = Step2Form(self)
        step2vis = Step2Visualizer(self)
        step2.grid(column=0, row=0)
        step2vis.grid(column=0, row=1)

        step2.add_on_calculate_listener(lambda v:self.on_calculate(v))

        self.form = step2
        self.visualization = step2vis
        self.image_getter = image_getter

    def on_calculate(self, v):
        angles = np.arange(v.min, v.max, v.step)

        results = implementation.radon(self.image_getter(), angles)

        self.visualization.set_options(list(angles), results)


