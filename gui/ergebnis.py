import tkinter as tk

class ResultWindow:
    def __init__(self, master, username, correct, total, category, difficulty, on_restart):
        self.master = master
        self.master.minsize(400, 300)
        self.frame = tk.Frame(master)
        self.frame.pack(padx=20, pady=20)
        tk.Label(self.frame, text=f"{username}, dein Ergebnis:").pack()
        tk.Label(self.frame, text=f"Kategorie: {category.capitalize()} | Schwierigkeit: {difficulty.capitalize()}").pack(pady=(5,0))
        tk.Label(self.frame, text=f"{correct} von {total} richtig").pack(pady=(5,10))
        tk.Button(self.frame, text="Neues Quiz", command=self.restart).pack()
        self.on_restart = on_restart
    def restart(self):
        self.frame.destroy()
        self.on_restart() 