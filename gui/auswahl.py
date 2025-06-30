import tkinter as tk

class SelectionWindow:
    def __init__(self, master, questions, on_select):
        self.master = master
        self.on_select = on_select
        self.frame = tk.Frame(master)
        self.frame.pack(padx=20, pady=20)
        categories = sorted(set(q["kategorie"] for q in questions))
        difficulties = sorted(set(q["schwierigkeit"] for q in questions))
        tk.Label(self.frame, text="Select category:").pack()
        self.cat_var = tk.StringVar(value=categories[0])
        for c in categories:
            tk.Radiobutton(self.frame, text=c, variable=self.cat_var, value=c).pack(anchor="w")
        tk.Label(self.frame, text="Select difficulty:").pack(pady=(10,0))
        self.diff_var = tk.StringVar(value=difficulties[0])
        for d in difficulties:
            tk.Radiobutton(self.frame, text=d, variable=self.diff_var, value=d).pack(anchor="w")
        tk.Button(self.frame, text="Start", command=self.select).pack(pady=10)
    def select(self):
        self.frame.destroy()
        self.on_select(self.cat_var.get(), self.diff_var.get()) 