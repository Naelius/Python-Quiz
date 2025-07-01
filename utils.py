import json
import os
import random
import re
from tkinter import messagebox

def get_available_pools(split_dir="data/split"):
    # Liefert eine Liste (Kategorie, Schwierigkeit) aus den Dateinamen
    pools = []
    for fname in os.listdir(split_dir):
        if fname.endswith(".json"):
            match = re.match(r"(.+)_([a-z]+)\.json", fname)
            if match:
                kat, lvl = match.groups()
                pools.append((kat, lvl))
    return pools

def load_questions_from_pool(category, difficulty, split_dir="data/split"):
    fname = f"{category}_{difficulty}.json"
    path = os.path.join(split_dir, fname)
    if not os.path.exists(path):
        messagebox.showerror("Error", f"Fragenpool {path} nicht gefunden.")
        return []
    with open(path, encoding="utf-8") as f:
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