# Tema pentru acasă - Lecția 13: Funcții Avansate (*args, **kwargs, lambda, closure, decoratori, recursivitate)

"""
Task: Creați o funcție cu numele "task_1" care acceptă orice număr de argumente numerice 
folosind *args și returnează suma tuturor argumentelor.
Exemplu: task_1(1, 2, 3) -> 6
         task_1(10, 20) -> 30
         task_1() -> 0
"""

# CODUL TĂU VINE MAI JOS:
def task_1(*args):
    return sum(args)
print(task_1())

# CODUL TĂU VINE MAI SUS:

"""
Task: Creați o funcție cu numele "task_2" care acceptă orice număr de argumente cu cuvinte cheie 
folosind **kwargs și returnează un dicționar cu toate cheile în majuscule.
Exemplu: task_2(nume="ana", varsta=25) -> {"NUME": "ana", "VARSTA": 25}
         task_2(oras="bucuresti", cod=123) -> {"ORAS": "bucuresti", "COD": 123}
"""

# CODUL TĂU VINE MAI JOS:
def task_2(**kwards):
    rezultat={}
    for nume, varsta in kwards.items():
       rezultat[nume.upper()]= varsta
    return rezultat
print(task_2(nume="ana", varsta=25))
# CODUL TĂU VINE MAI SUS:

"""
Task: Creați o funcție cu numele "task_3" care acceptă un nume obligatoriu, 
*args pentru hobby-uri și **kwargs pentru informații suplimentare.
Să returneze un string formatat: "Nume: [nume], Hobby-uri: [lista], Info: [dict]"
Exemplu: task_3("Ana", "citit", "alergat", varsta=25, oras="Cluj") -> 
         "Nume: Ana, Hobby-uri: ['citit', 'alergat'], Info: {'varsta': 25, 'oras': 'Cluj'}"
"""

# CODUL TĂU VINE MAI JOS:
def task_3(nume,*args,**kwards):
    return f'"Nume: {nume}, Hobby-uri: {args}, Info: {dict}"'
    
print(task_3("Nume: [Ana], Hobby-uri: [citit', 'alergat'], Info: {'varsta': 25, 'oras': 'Cluj'}"))
# CODUL TĂU VINE MAI SUS:

"""
Task: Creați o funcție lambda cu numele "task_4" care calculează pătratul unui număr.
Apoi creați o funcție cu numele "test_task_4" care aplică lambda-ul pe o listă de numere.
Exemplu: test_task_4([1, 2, 3, 4]) -> [1, 4, 9, 16]
"""

# CODUL TĂU VINE MAI JOS:
task_4=lambda x: x**2
def test_task_4 (lista_numere):
    return [task_4(numar) for numar in lista_numere]

print(test_task_4([5,4,6,8,9]))
# CODUL TĂU VINE MAI SUS:

"""
Task: Creați o funcție cu numele "task_5" care folosește map() și o funcție lambda 
pentru a converti o listă de temperature din Celsius în Fahrenheit.
Formula: F = C * 9/5 + 32
Exemplu: task_5([0, 20, 30]) -> [32.0, 68.0, 86.0]
"""

# CODUL TĂU VINE MAI JOS:

# CODUL TĂU VINE MAI SUS:

"""
Task: Creați o funcție cu numele "task_6" care folosește filter() și o funcție lambda 
pentru a filtra doar numerele pare dintr-o listă.
Exemplu: task_6([1, 2, 3, 4, 5, 6]) -> [2, 4, 6]
"""

# CODUL TĂU VINE MAI JOS:

# CODUL TĂU VINE MAI SUS:

"""
Task: Creați o funcție cu numele "task_7" care folosește sorted() și o funcție lambda 
pentru a sorta o listă de dicționare după vârstă.
Exemplu: task_7([{"nume": "Ana", "varsta": 25}, {"nume": "Ion", "varsta": 20}]) -> 
         [{"nume": "Ion", "varsta": 20}, {"nume": "Ana", "varsta": 25}]
"""

# CODUL TĂU VINE MAI JOS:

# CODUL TĂU VINE MAI SUS:

"""
Task: Creați o funcție cu numele "task_8" care returnează o funcție încapsulată.
Funcția principală primește un salut (default "Salut"), iar funcția încapsulată 
primește un nume și returnează salutul complet.
Exemplu: saluta = task_8("Bună ziua")
         saluta("Ana") -> "Bună ziua, Ana!"
"""

# CODUL TĂU VINE MAI JOS:

# CODUL TĂU VINE MAI SUS:

"""
Task: Creați o funcție cu numele "task_9" care implementează un contor folosind closure.
Funcția să returneze un dicționar cu două funcții: "increment" și "get_value".
Exemplu: contor = task_9()
         contor["increment"]() -> 1
         contor["increment"]() -> 2
         contor["get_value"]() -> 2
"""

# CODUL TĂU VINE MAI JOS:

# CODUL TĂU VINE MAI SUS:

"""
Task: Creați o funcție cu numele "task_10" care creează un multiplicator folosind closure.
Funcția primește un factor și returnează o funcție care înmulțește orice număr cu acel factor.
Exemplu: inmulteste_cu_3 = task_10(3)
         inmulteste_cu_3(5) -> 15
         inmulteste_cu_3(10) -> 30
"""

# CODUL TĂU VINE MAI JOS:

# CODUL TĂU VINE MAI SUS:

"""
Task: Creați un decorator simplu cu numele "task_11" care afișează un mesaj 
înainte și după executarea unei funcții.
Mesajul să fie: "Înainte de [nume_functie]" și "După [nume_functie]"
Testați-l pe o funcție simplă care afișează "Hello World!".
"""

# CODUL TĂU VINE MAI JOS:

# CODUL TĂU VINE MAI SUS:

"""
Task: Creați un decorator cu numele "task_12" care măsoară timpul de execuție al unei funcții.
Decoratorul să afișeze: "[nume_functie] a rulat în [timp] secunde"
Testați-l pe o funcție care calculează suma numerelor de la 1 la 1000000.
"""

# CODUL TĂU VINE MAI JOS:

# CODUL TĂU VINE MAI SUS:

"""
Task: Creați o funcție recursivă cu numele "task_13" care calculează suma numerelor 
de la 1 la n.
Exemplu: task_13(5) -> 15 (1+2+3+4+5)
         task_13(3) -> 6 (1+2+3)
"""

# CODUL TĂU VINE MAI JOS:

# CODUL TĂU VINE MAI SUS:

"""
Task: Creați o funcție recursivă cu numele "task_14" care calculează puterea unui număr.
Folosiți formula: a^n = a * a^(n-1), cu cazul de bază a^0 = 1.
Exemplu: task_14(2, 3) -> 8
         task_14(5, 2) -> 25
"""

# CODUL TĂU VINE MAI JOS:

# CODUL TĂU VINE MAI SUS:

"""
Task: Creați o funcție recursivă cu numele "task_15" care inversează un string.
Exemplu: task_15("hello") -> "olleh"
         task_15("python") -> "nohtyp"
"""

# CODUL TĂU VINE MAI JOS:

# CODUL TĂU VINE MAI SUS:

"""
Task: Creați o funcție cu numele "task_16" care combină *args, **kwargs și lambda.
Funcția să accepte o operație (string), *args pentru numere, și **kwargs pentru opțiuni.
Operațiile disponibile: "suma", "produs", "maxim", "minim".
Opțiunea "rotunjire" să specifice numărul de zecimale.
Exemplu: task_16("suma", 1, 2, 3, rotunjire=2) -> 6.00
         task_16("produs", 2, 3, 4) -> 24
"""

# CODUL TĂU VINE MAI JOS:

# CODUL TĂU VINE MAI SUS:

"""
Task: Creați o funcție cu numele "task_17" care implementează memoization pentru 
optimizarea funcțiilor recursive. Folosiți un dicționar pentru a stoca rezultatele calculate.
Aplicați-o pe funcția Fibonacci.
Exemplu: fibonacci_memo = task_17()
         fibonacci_memo(10) -> 55
         fibonacci_memo(15) -> 610
"""

# CODUL TĂU VINE MAI JOS:

# CODUL TĂU VINE MAI SUS:

"""
Task: Creați o funcție cu numele "task_18" care implementează un sistem de evenimente 
folosind closure. Funcția să returneze un dicționar cu metodele: "on", "emit", "off".
Exemplu: events = task_18()
         events["on"]("user_login", lambda user: print(f"Utilizator logat: {user}"))
         events["emit"]("user_login", "Ana") -> "Utilizator logat: Ana"
"""

# CODUL TĂU VINE MAI JOS:

# CODUL TĂU VINE MAI SUS:

"""
Task: Creați o funcție cu numele "task_19" care implementează un decorator parametrizat 
pentru limitarea numărului de apeluri ale unei funcții.
Decoratorul să primească max_calls și să afișeze o eroare dacă funcția e apelată prea des.
Exemplu: @task_19(max_calls=3)
         def saluta(): print("Salut!")
"""

# CODUL TĂU VINE MAI JOS:

# CODUL TĂU VINE MAI SUS:

"""
Task: Creați o funcție cu numele "task_20" care implementează un analizator de text complex.
Funcția să accepte *texte și **opțiuni, să folosească lambda pentru procesare, 
și să returneze statistici complete.
Opțiuni: "include_stats", "min_word_length", "ignore_case"
Să calculeze: numărul de cuvinte, numărul de caractere, cuvintele unice, etc.
Exemplu: task_20("Hello world", "Python rocks", include_stats=True, min_word_length=3)
"""

# CODUL TĂU VINE MAI JOS:

# CODUL TĂU VINE MAI SUS:

# Testare opțională - decomentează pentru a testa funcțiile
"""
# Test task_1
print("=== TEST TASK_1 ===")
print(task_1(1, 2, 3))
print(task_1(10, 20))
print(task_1())

# Test task_4
print("=== TEST TASK_4 ===")
print(test_task_4([1, 2, 3, 4]))

# Test task_8
print("=== TEST TASK_8 ===")
saluta = task_8("Bună ziua")
print(saluta("Ana"))
"""