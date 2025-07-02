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

#EXERCITIUL NUMRUL 2!!!
class HarshadNumber:
    def __init__(self, number):
        self.number = number

    def sum_of_digits(self):
        return sum(int(digit) for digit in str(self.number))

    def is_harshad(self):
        digit_sum = self.sum_of_digits()
        if digit_sum == 0:
            return False 
        return self.number % digit_sum == 0
    


if __name__ == "__main__":
    num = int(45)
    checker = HarshadNumber(num)
    if checker.is_harshad():
        print(f"{num} este un număr Harshad.")
    else:
        print(f"{num} nu este un număr Harshad.")    