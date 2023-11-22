import tkinter
from step_3 import Step3
from step_2 import Step2
from input_panel import InputPanel

root = tkinter.Tk()
root.wm_title("TP8")

props = {"padx": 10.0, "pady": 10.0}

input_panel = InputPanel(root)
input_panel.grid(column=0, row=0, **props)

step2 = Step2(lambda:input_panel.image.get_image(), root)
step2.grid(column=1, row=0, **props)

step3 = Step3(step2, root)
step3.grid(column=2, row=0, **props)

tkinter.mainloop()
