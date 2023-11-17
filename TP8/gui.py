import tkinter
from step_2 import Step2
from input_panel import InputPanel

root = tkinter.Tk()
root.wm_title("TP8")


input_panel = InputPanel(root)
input_panel.grid(column=0, row=0)

step2 = Step2(root)
step2.grid(column=1, row=0)

tkinter.mainloop()
