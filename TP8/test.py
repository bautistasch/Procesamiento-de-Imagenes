import tkinter as tk
 
root = tk.Tk()

         
 
class Test(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)

        # def write_callback(var, index, mode):
            # print("The variable has been written to in mode:", mode)
        var = tk.StringVar()
        var.set('0.1')
        var.trace_add("write", callback=self.write_callback)
         
        entry_widget = tk.Entry(self, textvariable=var)
        # entry_widget.pack(expand=True, fill=tk.BOTH)
        entry_widget.grid(padx=20, pady=20)
        self.var = var
    def write_callback(self, var,  index, mode):
        print("The variable has been written to in mode:", mode)
 
# class Test2(tk.Frame):
    # def __init__(self, master = None):
        # super().__init__(master)

        # entry_widget = Test(self)
        # entry_widget.pack(expand=True, fill=tk.BOTH)

test = Test(root)
test.pack()

root.mainloop()
