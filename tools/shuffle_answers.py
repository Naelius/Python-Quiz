import json
import random

with open('data/quiz.json', encoding='utf-8') as f:
    fragen = json.load(f)

for frage in fragen:
    richtige_antwort = frage['antworten'][frage['richtig']]
    random.shuffle(frage['antworten'])
    frage['richtig'] = frage['antworten'].index(richtige_antwort)

with open('data/quiz.json', 'w', encoding='utf-8') as f:
    json.dump(fragen, f, ensure_ascii=False, indent=2) 