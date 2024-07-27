import random

numeros = random.sample(range(1,101), 20)

Imp = []
Par = []

for numero in numeros:
    if numero % 2 == 0:
        Par.append(numero)
    else:
        Imp.append(numero)
        
print(f'Os numeros impares são: {Imp}')
print(f'Os numeros pares são: {Par}')


        
        


