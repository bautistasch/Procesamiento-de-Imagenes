import tkinter as tk
from step_2_form import Step2Form
from step_2_visualizer import Step2Visualizer
import numpy as np

class Step2(tk.Frame):
    on_calculate_listeners = []

    def __init__(self, master=None):
        super().__init__(master)
        
        step2 = Step2Form(self)
        step2vis = Step2Visualizer(self)
        step2.grid(column=0, row=0)
        step2vis.grid(column=0, row=1)

        step2.add_on_calculate_listener(lambda v:step2vis.set_options(list(map(int, np.arange(v.min, v.max, v.step)))))
