from utils import load_questions, save_result
from gui.login import LoginWindow
from gui.auswahl import SelectionWindow
from gui.quiz import QuizWindow
from gui.ergebnis import ResultWindow
import tkinter as tk
import random

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz Tool")
        self.questions = load_questions("data/quiz.json")
        self.username = None
        self.show_login()
    def show_login(self):
        LoginWindow(self.master, self.on_login)
    def on_login(self, username):
        self.username = username
        self.show_selection()
    def show_selection(self):
        SelectionWindow(self.master, self.questions, self.on_selection)
    def on_selection(self, category, difficulty):
        filtered = [q for q in self.questions if q["kategorie"] == category and q["schwierigkeit"] == difficulty]
        num_questions = 5
        if len(filtered) > num_questions:
            filtered = random.sample(filtered, num_questions)
        if not filtered:
            from tkinter import messagebox
            messagebox.showinfo("Hint", "No questions for this selection.")
            self.show_selection()
            return
        QuizWindow(self.master, filtered, self.username, self.on_end)
    def on_end(self, correct, total):
        save_result(self.username, {
            "benutzer": self.username,
            "richtig": correct,
            "gesamt": total
        }, filepath="data/user_results.json")
        ResultWindow(self.master, self.username, correct, total, self.show_selection)

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop() 