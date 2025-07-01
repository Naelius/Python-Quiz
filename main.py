from utils import get_available_pools, load_questions_from_pool, save_result
from gui.login import LoginWindow
from gui.auswahl import SelectionWindow
from gui.quiz import QuizWindow
from gui.ergebnis import ResultWindow
import tkinter as tk
import random

def readable(text):
    # Macht aus z.B. powershell_leicht -> PowerShell (leicht)
    parts = text.split('_')
    if len(parts) == 2:
        kat, lvl = parts
        return f"{kat.capitalize()} ({lvl})"
    return text.capitalize()

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz Tool")
        self.pools = get_available_pools()
        self.username = None
        self.show_login()
    def show_login(self):
        LoginWindow(self.master, self.on_login)
    def on_login(self, username):
        self.username = username
        self.show_selection()
    def show_selection(self):
        # Extrahiere Kategorien und Schwierigkeitsgrade aus den Pools
        kategorien = sorted(set(k for k, _ in self.pools))
        schwierigkeitsgrade = sorted(set(l for _, l in self.pools))
        # Zeige Auswahlfenster
        SelectionWindow(self.master, self.pools, self.on_selection)
    def on_selection(self, category, difficulty):
        questions = load_questions_from_pool(category, difficulty)
        num_questions = 5
        if len(questions) > num_questions:
            questions = random.sample(questions, num_questions)
        if not questions:
            from tkinter import messagebox
            messagebox.showinfo("Hinweis", "Keine Fragen für diese Auswahl.")
            self.show_selection()
            return
        QuizWindow(
            self.master,
            questions,
            self.username,
            lambda correct, total, category, difficulty: self.on_end(correct, total, category, difficulty),
            category,
            difficulty
        )
    def on_end(self, correct, total, category, difficulty):
        save_result(self.username, {
            "benutzer": self.username,
            "kategorie": category,
            "schwierigkeit": difficulty,
            "richtig": correct,
            "gesamt": total
        }, filepath="data/user_results.json")
        ResultWindow(self.master, self.username, correct, total, category, difficulty, self.show_selection)

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop() 