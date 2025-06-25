# START TASK - Lecția 5.3 Funcții Lambda și Closures
# Timp estimat: 20 minute
# Branch: start-task-lesson-5-3

# Exercițiul 1: Creați o funcție lambda care adună două numere
adunare = None  # ÎNLOCUIEȘTE None cu lambda function
adunare = lambda x, y: x + y
    

print(adunare(5,3))
print(adunare(10,2))
# Testare:
# print(adunare(5, 3))    # Ar trebui să afișeze 8
# print(adunare(10, 2))   # Ar trebui să afișeze 12


# Exercițiul 2: Creați o funcție lambda care verifică dacă un număr este par
este_par = None  # ÎNLOCUIEȘTE None cu lambda function

este_par=lambda x:x % 2==0
print(este_par(5)) 
print(este_par(4))      # Ar trebui să afișeze True
print(este_par(5))      # Ar trebui să afișeze False


# Exercițiul 3: Folosiți lambda cu filter pentru a găsi numerele mari
# Filtrați numerele mai mari decât 10 din lista de mai jos
numere = [5, 12, 8, 15, 3, 20, 7]

numere_mari = list(filter(lambda x: x>10, numere))
print(numere_mari)


# Exercițiul 4: Creați o funcție simplă care conține o funcție internă
# Funcția principală să se numească "salut_creator"
# Funcția internă să se numească "spune_salut" și să printeze "Bună ziua!"
def salut_creator():
   def spune_salut():
        print('Buna ziua!')
   spune_salut()
   

# Testare:
salut_creator()  # Ar trebui să afișeze "Bună ziua!"


# Exercițiul 5: CLOSURE - Creați un counter simplu
# Funcția să returneze o funcție internă care numără de câte ori a fost apelată
def creeaza_counter():
    # CODUL TĂU AICI
 counter=0
 def count():
    nonlocal counter
    print(f'functia a fost apelata de {counter} ori')
    counter += 1
    return counter
 return count


# Testare:
counter1 = creeaza_counter()
print(counter1())  # Ar trebui să afișeze 1
print(counter1())  # Ar trebui să afișeze 2
print(counter1())  # Ar trebui să afișeze 3


# Exercițiul 6: CLOSURE - Creator de funcții de înmulțire
# Funcția să primească un număr și să returneze o funcție care înmulțește cu acel număr
def creeaza_inmultitor(factor):
   return lambda x: x*factor



    # CODUL TĂU AICI
 


inmulteste_cu_2 = creeaza_inmultitor(2)
inmulteste_cu_5 = creeaza_inmultitor(5)
print(inmulteste_cu_2(10))  # Ar trebui să afișeze 20 (10 * 2)
print(inmulteste_cu_5(3))   # Ar trebui să afișeze 15 (3 * 5)