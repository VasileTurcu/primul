# START TASK - Fișiere, OS și JSON (10-15 minute)

# Exercițiul 1: Creează un fișier text cu informații despre tine
# Scrie un program care creează un fișier "despre_mine.txt" cu următoarele informații:
# - Numele tău
# - Vârsta ta
# - Orașul tău
# - 2 hobby-uri
# Folosește '\n' pentru a separa fiecare informație pe o linie nouă
with open("despre_mine.txt", "w", encoding="utf-8") as f:
    f.write("Nume: Vasile Turcu\n")
    f.write("Vârsta: 23\n")
    f.write("Oraș: Balti\n")
    f.write("Hobby-uri: Sport, Filme\n")
print("Fișierul 'despre_mine.txt' a fost creat.")

# Exercițiul 2: Citește și afișează conținutul fișierului
# Scrie un program care citește fișierul "despre_mine.txt" și afișează conținutul

with open("despre_mine.txt", "r", encoding="utf-8") as f:
    content = f.read()
print("Conținutul fișierului:")
print(content)
# Exercițiul 3: Folosește modulul OS pentru a verifica dimensiunea fișierului
# Importă modulul os și verifică:
# - Dacă fișierul "despre_mine.txt" există
# - Care este dimensiunea fișierului în bytes
import os
if os.path.exists("despre_mine.txt"):
    size = os.path.getsize("despre_mine.txt")
    print(f"Fișierul există și are dimensiunea de {size} bytes.")
else:
    print("Fișierul nu există.")
# Exercițiul 4: Creează un dicționar și salvează-l în JSON
# Creează un dicționar cu aceleași informații despre tine și salvează-l într-un fișier "date.json"
import json

date = {
    "nume": "Turcu Vasile",
    "varsta": 23,
    "oras": "Balti",
    "hobbyuri": ["Sport", "Filme"]
}

with open("date.json", "w", encoding="utf-8") as f:
    json.dump(date, f, ensure_ascii=False, indent=4)

print("Fișierul 'date.json' a fost creat.")

# Exercițiul 5: Citește și afișează datele din JSON
# Încarcă datele din "date.json" și afișează-le într-un format frumos