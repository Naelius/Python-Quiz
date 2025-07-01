import json
import random
import os

# Shuffle alle JSON-Dateien im data/split/-Ordner
split_dir = 'data/split'
for fname in os.listdir(split_dir):
    if fname.endswith('.json'):
        path = os.path.join(split_dir, fname)
        with open(path, encoding='utf-8') as f:
            fragen = json.load(f)
        for frage in fragen:
            richtige_antwort = frage['antworten'][frage['richtig']]
            random.shuffle(frage['antworten'])
            frage['richtig'] = frage['antworten'].index(richtige_antwort)
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(fragen, f, ensure_ascii=False, indent=2)
print('Alle Fragenpools in data/split/ wurden geshuffelt.') 