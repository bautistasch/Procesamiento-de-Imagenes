import tkinter

from input_panel import InputPanel
from step_2_form import Step2Form

root = tkinter.Tk()
root.wm_title("TP8")


input_panel = InputPanel(root)
input_panel.grid(column=0, row=0)

step2 = Step2Form(root)
step2.grid(column=1, row=0)

tkinter.mainloop()
