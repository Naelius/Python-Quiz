import tkinter as tk
from tkinter import messagebox
import random

class QuizWindow:
    def __init__(self, master, questions, username, on_end):
        self.master = master
        self.questions = questions
        self.username = username
        self.on_end = on_end
        self.index = 0
        self.correct = 0
        random.shuffle(self.questions)
        self.frame = tk.Frame(master)
        self.frame.pack(padx=20, pady=20)
        self.question_label = tk.Label(self.frame, text="", wraplength=400, justify="left")
        self.question_label.pack()
        self.var = tk.IntVar()
        self.answer_buttons = []
        for i in range(4):
            btn = tk.Radiobutton(self.frame, text="", variable=self.var, value=i)
            btn.pack(anchor="w")
            self.answer_buttons.append(btn)
        self.feedback = tk.Label(self.frame, text="")
        self.feedback.pack(pady=(5,0))
        self.next_btn = tk.Button(self.frame, text="Next", command=self.next_question)
        self.next_btn.pack(pady=10)
        self.show_question()
    def show_question(self):
        if self.index >= len(self.questions):
            self.frame.destroy()
            self.on_end(self.correct, len(self.questions))
            return
        question = self.questions[self.index]
        self.question_label.config(text=question["frage"])
        for i, text in enumerate(question["antworten"]):
            self.answer_buttons[i].config(text=text)
        self.var.set(-1)
        self.feedback.config(text="")
    def next_question(self):
        if self.var.get() == -1:
            messagebox.showinfo("Hint", "Please select an answer.")
            return
        question = self.questions[self.index]
        if self.var.get() == question["richtig"]:
            self.correct += 1
            self.feedback.config(text="Correct!", fg="green")
        else:
            self.feedback.config(text=f"Wrong! Correct answer: {question['antworten'][question['richtig']]}", fg="red")
        self.master.after(1000, self._next)
    def _next(self):
        self.index += 1
        self.show_question() 