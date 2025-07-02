# START TASK - Lecția OOP1: Clase și Obiecte
# Timp estimat: 20 minute
# Obiectiv: Înțelegerea conceptelor de bază ale OOP în Python

print("=== START TASK - OOP1: CLASE ȘI OBIECTE ===\n")

# Exercițiul 1: Prima ta clasă
# Creează o clasă simplă numită "Persoana" cu:
# - Un atribut "nume" și "varsta"
# - O metodă "saluta" care printează un mesaj de salut

class Persoana:
    def __init__(self, nume, varsta):
        self.nume = nume
        self.varsta=varsta
    
    def saluta(self):
        print(f"Salut, mă numesc {self.nume} și am {self.varsta} ani")
       

# Testare Exercițiul 1:
persoana1 = Persoana("Ana", 25)
persoana1.saluta()



# Exercițiul 2: Clasa Câine
# Creează o clasă "Caine" cu:
# - Atribute: nume, rasa, varsta
# - Metode: latra(), doarme(), joaca()

class Caine:
    def __init__(self, nume, rasa, varsta):
        self.nume = nume
        self.rasa = rasa
        self.varsta = varsta
    
    def latra(self):
        print(f"{self.nume} face: Ham! Ham!")
    
    def doarme(self):
        print(f"{self.nume} doarme liniștit...")
    
    def joaca(self):
        print(f"{self.nume} se joacă cu mingea!")

# Testare Exercițiul 2:
rex = Caine("Rex", "Golden Retriever", 3)
rex.latra()
rex.doarme()
rex.joaca()


# Exercițiul 3: Clasa Calculator Simplu
# Creează o clasă "Calculator" cu:
# - Un atribut "rezultat" (inițial 0)
# - Metode: aduna(numar), scade(numar), afiseaza_rezultat()

class Calculator:
    def __init__(self):
        self.rezultat = 0  

    def aduna(self, numar):
        self.rezultat += numar  

    def scade(self, numar):
        self.rezultat -= numar  

    def afiseaza_rezultat(self):
        print(f"Rezultatul curent este: {self.rezultat}")

# Testare Exercițiul 3:
calc = Calculator()
calc.aduna(10)
calc.aduna(5)
calc.scade(3)
calc.afiseaza_rezultat()  


# Exercițiul 4: Clasa Carte
# Creează o clasă "Carte" cu:
# - Atribute: titlu, autor, numar_pagini
# - Metode: afiseaza_info(), este_groasa() (returnează True dacă are >300 pagini)

class Carte:
    def __init__(self, titlu, autor, numar_pagini):
        # COMPLETEAZĂ AICI
        pass
    
    def afiseaza_info(self):
        # COMPLETEAZĂ AICI - afișează toate informațiile despre carte
        pass
    
    def este_groasa(self):
        # COMPLETEAZĂ AICI - returnează True dacă cartea are peste 300 de pagini
        pass

# Testare Exercițiul 4:
# carte1 = Carte("1984", "George Orwell", 350)
# carte1.afiseaza_info()
# print(f"Este o carte groasă? {carte1.este_groasa()}")