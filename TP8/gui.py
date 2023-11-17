import tkinter

from input_panel import InputPanel

root = tkinter.Tk()
root.wm_title("TP8")


input_panel = InputPanel(root)
input_panel.pack()

tkinter.mainloop()
