import json
import os
import random
from tkinter import messagebox

def load_questions(filepath):
    if not os.path.exists(filepath):
        messagebox.showerror("Error", f"File {filepath} not found.")
        return []
    with open(filepath, encoding="utf-8") as f:
        fragen = json.load(f)
    # Shuffle answers for each question and update the correct index
    for frage in fragen:
        richtige_antwort = frage['antworten'][frage['richtig']]
        random.shuffle(frage['antworten'])
        frage['richtig'] = frage['antworten'].index(richtige_antwort)
    return fragen

def save_result(username, result, filepath="data/user_results.json"):
    data = []
    if os.path.exists(filepath):
        with open(filepath, encoding="utf-8") as f:
            data = json.load(f)
    data.append(result)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2) 