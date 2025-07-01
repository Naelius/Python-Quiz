import tkinter as tk
from tkinter import messagebox
import random

class QuizWindow:
    def __init__(self, master, questions, username, on_end, category=None, difficulty=None):
        self.master = master
        self.master.minsize(500, 400)
        self.questions = questions
        self.username = username
        self.on_end = on_end
        self.category = category
        self.difficulty = difficulty
        self.index = 0
        self.correct = 0
        random.shuffle(self.questions)
        self.frame = tk.Frame(master)
        self.frame.pack(padx=20, pady=20)
        self.question_label = tk.Label(self.frame, text="", wraplength=400, justify="left", font=("Arial", 13, "bold"))
        self.question_label.pack(pady=(0,10))
        self.card_frame = tk.Frame(self.frame)
        self.card_frame.pack(pady=10)
        self.cards = []
        self.selected = None
        self.next_btn = tk.Button(self.frame, text="Next", state="disabled", command=self.next_question)
        self.next_btn.pack(pady=10)
        self.feedback = tk.Label(self.frame, text="", font=("Arial", 11))
        self.feedback.pack(pady=(5,0))
        self.show_question()

    def show_question(self):
        if self.index >= len(self.questions):
            self.frame.destroy()
            self.on_end(self.correct, len(self.questions), self.category, self.difficulty)
            return
        question = self.questions[self.index]
        self.question_label.config(text=question["frage"])
        # Antworten als Card-Style
        for widget in self.card_frame.winfo_children():
            widget.destroy()
        self.cards = []
        self.selected = None
        for i, text in enumerate(question["antworten"]):
            card = tk.Label(self.card_frame, text=text, width=40, height=2, relief="raised", bd=2, bg="white", font=("Arial", 11))
            card.pack(pady=6)
            card.bind("<Button-1>", lambda e, idx=i: self.select(idx))
            card.bind("<Enter>", lambda e, idx=i: self.hover(idx, True))
            card.bind("<Leave>", lambda e, idx=i: self.hover(idx, False))
            self.cards.append(card)
        self.next_btn.config(state="disabled")
        self.feedback.config(text="")

    def select(self, idx):
        self.selected = idx
        for i, card in enumerate(self.cards):
            if i == idx:
                card.config(bg="#4fa3f7", fg="white", relief="solid", bd=3)
            else:
                card.config(bg="white", fg="black", relief="raised", bd=2)
        self.next_btn.config(state="normal")
        self.feedback.config(text="")

    def hover(self, idx, enter):
        if self.selected == idx:
            return
        if enter:
            self.cards[idx].config(bg="#e0eaff")
        else:
            self.cards[idx].config(bg="white")

    def next_question(self):
        if self.selected is None:
            messagebox.showinfo("Hinweis", "Bitte eine Antwort auswählen.")
            return
        question = self.questions[self.index]
        if self.selected == question["richtig"]:
            self.correct += 1
            self.feedback.config(text="Richtig!", fg="green")
        else:
            self.feedback.config(text=f"Falsch! Richtige Antwort: {question['antworten'][question['richtig']]}", fg="red")
        self.next_btn.config(state="disabled")
        self.master.after(1000, self._next)

    def _next(self):
        self.index += 1
        self.show_question() 