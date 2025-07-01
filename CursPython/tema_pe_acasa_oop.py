count=0
numele= 'Turcu Vasile'
for i in numele:
    parametri= ord(i)
    print(f"'{i}' -> {parametri}")
    count+=parametri


suma=(count % 3) + 1
print(f'suma valorilor ASCII pentru fiecare caracter va fi:{count}')
print(f'varianta după formula: {suma}')