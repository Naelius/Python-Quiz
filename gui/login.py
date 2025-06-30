import tkinter as tk
from tkinter import messagebox

class LoginWindow:
    def __init__(self, master, on_login):
        self.master = master
        self.on_login = on_login
        self.frame = tk.Frame(master)
        self.frame.pack(padx=20, pady=20)
        tk.Label(self.frame, text="Username:").pack()
        self.entry = tk.Entry(self.frame)
        self.entry.pack()
        tk.Button(self.frame, text="Login", command=self.login).pack(pady=10)
    def login(self):
        name = self.entry.get().strip()
        if not name:
            messagebox.showwarning("Error", "Please enter a username.")
            return
        self.frame.destroy()
        self.on_login(name) 