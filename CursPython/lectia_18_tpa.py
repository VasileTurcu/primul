"""
Tema pentru acasă: Moștenirea și Polimorfismul în Python

Cerințe:
Creați un proiect care să îmbine noțiunile de moștenire și polimorfism. Respectați pașii de mai jos pentru
 a implementa o aplicație simplă de gestionare a vehiculelor și a caracteristicilor acestora.

1. Clasa de bază Vehicle
Definiți clasa de bază Vehicle cu următoarele atribute:
- brand (string): marca vehiculului.
- model (string): modelul vehiculului.
- year (int): anul de fabricație.
Adăugați metoda:
- get_info(): Returnează un string cu toate informațiile despre vehicul în formatul:
"{brand} {model}, fabricat în anul {year}".

2. Clase derivate
a) Clasa Car
    Moștenește clasa Vehicle.
    Constructorul primește:
        - Toate atributele din clasa Vehicle.
        - fuel_type (string): tipul de combustibil (ex.: benzină, motorină, electric).
        - doors (int): numărul de uși.
    * Suprascrie metoda get_info() pentru a include și fuel_type și doors.
    Exemplu de mesaj returnat:
    "Tesla Model S, fabricat în anul 2022, electric, cu 4 uși."

b) Clasa Bicycle
    Moștenește clasa Vehicle.
    Constructorul primește:
        - Toate atributele din clasa Vehicle.
        - type (string): tipul bicicletei (ex.: șosea, MTB, pliabilă).
        - gear_count (int): numărul de viteze.
    * Suprascrie metoda get_info() pentru a include type și gear_count.
    Exemplu de mesaj returnat:
    "Merida Crossway, fabricat în anul 2021, tip: șosea, cu 21 viteze."

c) Clasa Motorcycle
    Moștenește clasa Vehicle.
    Constructorul primește:
        - Toate atributele din clasa Vehicle.
        - engine_capacity (int): capacitatea motorului (cm³).
        - has_sidecar (bool): dacă motocicleta are sau nu ataș.
    * Suprascrie metoda get_info() pentru a include engine_capacity și has_sidecar.
    Exemplu de mesaj returnat:
    "Honda Shadow, fabriat în anul 2020, motor de 745 cm³, fără ataș."

3. Cerințe suplimentare
Creați o listă de vehicule care să includă cel puțin câte un exemplu din fiecare
clasă (Car, Bicycle, Motorcycle).
Parcurgeți lista și afișați informațiile pentru fiecare vehicul utilizând metoda get_info().
"""
# 1. Clasa de bază Vehicle
# Definiți clasa de bază Vehicle cu următoarele atribute:
# - brand (string): marca vehiculului.
# - model (string): modelul vehiculului.
# - year (int): anul de fabricație.
# Adăugați metoda:
# - get_info(): Returnează un string cu toate informațiile despre vehicul în formatul:
# "{brand} {model}, fabricat în anul {year}".

class Vehicle:
    def __init__(self, brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    def get_info(self):
        return f" Vehiculul {self.brand} cu modelul {self.model} a fost produs in anul {self.year}"

class Car(Vehicle):
    def __init__(self,brand,model,year,fuel_type,doors):
        super().__init__(brand,model,year)
        self.fuel_type= fuel_type
        self.doors= doors
    def get_info(self):
        return f" Vehiculul {self.brand} cu modelul {self.model} a fost produs in anul {self.year} are {self.doors} si foloseste ca combustibil {self.fuel_type}"

class Bicycle(Vehicle):
    def __init__(self,brand,model,year,type,gear_count):
        super().__init__(brand,model,year)
        self.type=type
        self.gear_count = gear_count
    def get_info(self):
        return f" Bicicleta {self.brand} cu modelul {self.model} a fost produs in anul {self.year} este de tip {self.type} cu {self.gear_count} viteze"

class Motorcycle(Vehicle):
    def __init__(self,brand,model,year,engine_capacity,has_sidecar):
        super().__init__(brand,model,year)
        self.engine_capacity=engine_capacity
        self.has_sidecar=has_sidecar
    def get_info(self):
        sidecar_status= "cu ataș" if self.has_sidecar else "fără ataș"
        return f" Vehiculul {self.brand} cu modelul {self.model} a fost produs in anul {self.year} are motorul {self.engine_capacity} si este {sidecar_status}"
vehicule = [
    Car("Tesla", "Model S", 2022, "electric", 4),
    Bicycle("Merida", "Crossway" , 2021, "șosea", 21 ),
    Motorcycle("Honda ", "Shadow",  2020,  745 , False)]


for vehicul in vehicule:
    print(vehicul.get_info())