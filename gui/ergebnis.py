import tkinter as tk

class ResultWindow:
    def __init__(self, master, username, correct, total, on_restart):
        self.master = master
        self.frame = tk.Frame(master)
        self.frame.pack(padx=20, pady=20)
        tk.Label(self.frame, text=f"{username}, your result:").pack()
        tk.Label(self.frame, text=f"{correct} out of {total} correct").pack(pady=(5,10))
        tk.Button(self.frame, text="New Quiz", command=self.restart).pack()
        self.on_restart = on_restart
    def restart(self):
        self.frame.destroy()
        self.on_restart() 