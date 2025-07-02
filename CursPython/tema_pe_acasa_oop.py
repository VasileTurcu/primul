#EXERCITIUL NUMRUL 1!!!
count=0
numele= 'Turcu Vasile'
for i in numele:
    parametri= ord(i)
    print(f"'{i}' -> {parametri}")
    count+=parametri


suma=(count % 3) + 1
print(f'suma valorilor ASCII pentru fiecare caracter va fi:{count}')
print(f'varianta după formula: {suma}')

#EXERCITIUL NUMRUL 2!!!
class NumarSpecial:
    def __init__(self, number):
        self.number = number
        self.is_special = False

    def check(self):
       suma= sum(int(num)** 3 for num in str(self.number))
       self.numar_special = suma==self.number

        

    def print_state(self):
        # Afișați rezultatul verificării
        if self.numar_special:
            print(f'{self.number} este un numar Armstrong')
        else:
            print(f'{self.number} nu este un numar Armstrong')
numar1= NumarSpecial (45)
numar1.check()
numar1.print_state()