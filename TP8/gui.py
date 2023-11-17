import tkinter
from step_3 import Step3
from step_2 import Step2
from input_panel import InputPanel

root = tkinter.Tk()
root.wm_title("TP8")


input_panel = InputPanel(root)
input_panel.grid(column=0, row=0)

step2 = Step2(root)
step2.grid(column=1, row=0)

step3 = Step3(step2, root)
step3.grid(column=2, row=0)

tkinter.mainloop()
