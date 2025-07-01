import tkinter as tk
import os

class SelectionWindow:
    def __init__(self, master, pools, on_select):
        self.master = master
        self.master.minsize(400, 300)
        self.on_select = on_select
        self.pools = pools
        self.selected_category = None
        self.selected_level = None
        self.categories = sorted(set(k for k, _ in pools))
        self.levels_by_category = {k: sorted(l for k2, l in pools if k2 == k) for k in self.categories}
        self.frame = tk.Frame(master)
        self.frame.pack(padx=20, pady=20)
        tk.Label(self.frame, text="Kategorie wählen:", font=("Arial", 12, "bold")).pack(pady=(0,5))
        self.cat_frame = tk.Frame(self.frame)
        self.cat_frame.pack(pady=(0,10))
        self.cat_cards = {}
        for k in self.categories:
            card = tk.Label(self.cat_frame, text=k.capitalize(), width=16, height=2, relief="raised", bd=2, bg="white")
            card.pack(side="left", padx=8, pady=5)
            card.bind("<Button-1>", lambda e, name=k: self.select_category(name))
            self.cat_cards[k] = card
        self.level_label = tk.Label(self.frame, text="", font=("Arial", 12, "bold"))
        self.level_frame = tk.Frame(self.frame)
        self.level_cards = {}
        self.start_btn = tk.Button(self.frame, text="Start", command=self.start)
        self.start_btn_is_packed = False

    def select_category(self, name):
        self.selected_category = name
        for k, card in self.cat_cards.items():
            if k == name:
                card.config(bg="#4fa3f7", fg="white", relief="solid", bd=3)
            else:
                card.config(bg="white", fg="black", relief="raised", bd=2)
        # Schwierigkeitsgrade anzeigen
        self.level_label.pack_forget()
        self.level_frame.pack_forget()
        self.level_label.config(text="Schwierigkeitsgrad wählen:")
        self.level_label.pack(pady=(10,5))
        self.level_frame = tk.Frame(self.frame)
        self.level_frame.pack(pady=(0,10))
        for widget in self.level_frame.winfo_children():
            widget.destroy()
        self.level_cards = {}
        for l in self.levels_by_category[name]:
            card = tk.Label(self.level_frame, text=l.capitalize(), width=16, height=2, relief="raised", bd=2, bg="white")
            card.pack(side="left", padx=8, pady=5)
            card.bind("<Button-1>", lambda e, level=l: self.select_level(level))
            self.level_cards[l] = card
        self.selected_level = None
        if self.start_btn_is_packed:
            self.start_btn.pack_forget()
            self.start_btn_is_packed = False

    def select_level(self, level):
        self.selected_level = level
        for l, card in self.level_cards.items():
            if l == level:
                card.config(bg="#4fa3f7", fg="white", relief="solid", bd=3)
            else:
                card.config(bg="white", fg="black", relief="raised", bd=2)
        if not self.start_btn_is_packed:
            self.start_btn.pack(in_=self.frame, after=self.level_frame, pady=10)
            self.start_btn_is_packed = True

    def start(self):
        self.frame.destroy()
        self.on_select(self.selected_category, self.selected_level) 