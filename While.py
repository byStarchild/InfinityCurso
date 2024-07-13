
#Aula de While

#contador = 0

#while contador < 5: #enquanto o contador for menor que cinco, faça algo
    #print(contador)
    #contador += 1   #enquanto meu contador for menor que cinco, adicione mais um
    #break

#soma = 0
#limite = 10

#while soma< limite:
    #numero_iu = int(input("Digite um numero: "))
    #soma += numero
    
#print(f"a soma ultrapassou o numero de {limite}, a soma final é {soma}")#

#5numero = 0 
#limite = 10

#while numero < limite:
#    print(numero)
#    numero += 2
#    break

#import random

#numero_aleatorio = random.randint(1, 20)
#numero_tentativas = 0

#print("Vamos jogar advinhe o numero que estou pensando entre um e vinte!")

#while numero_tentativas != numero_aleatorio:
#    numero_tentativas = int(input("Digite um numero: "))
    
#    if numero_tentativas == numero_aleatorio:
#        print(f"Parabens, você acertou! o numero era {numero_tentativas}")
#        break
#    elif numero_tentativas < numero_aleatorio:
#        print("Tente chutar um pouco mais alto...")
#    elif numero_tentativas > numero_aleatorio:
#        print("Tente chutar um pouco mais baixo...")

import random

nomes = ['João', 'Hamilton', 'Pedro', 'Vinicius', 'Carlos']
interrogado = random.choice(nomes)

print("Vamos jogar um jogo de detetive.")
print("Houve um crime no beco dos Falangeiros. A suspeita é que houve uma briga após a saída de um bar, estima-se ser um acerto de contas e um crime premeditado. Estamos investigando...")
print(f"O suspeito a ser interrogado é: {interrogado}")

pergunta_1 = input("Telefonou para a vítima? (sim/não) ")
pergunta_2 = input("Esteve no local do crime? (sim/não) ")    
pergunta_3 = input("Mora perto da vítima? (sim/não) ")
pergunta_4 = input("Devia para a vítima? (sim/não) ")
pergunta_5 = input("Já trabalhou com a vítima? (sim/não) ")

classificador = 0

if pergunta_1 == "sim":
    classificador += 1   
if pergunta_2 == "sim":
    classificador += 1    
if pergunta_3 == "sim":
    classificador += 1    
if pergunta_4 == "sim":
    classificador += 1    
if pergunta_5 == "sim":
    classificador += 1
    
if classificador == 2:
    participacao = "suspeito"
elif classificador == 3 or classificador == 4:
    participacao = "cúmplice"
elif classificador == 5:
    participacao = "assassino"
else:
    participacao = "inocente"
    
print(f"O {interrogado} foi classificado como {participacao}, baseado nas perguntas feitas com relação à vítima.")

#soma de três números usando WHILE

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segunda número: "))
num3 = float(input("Digite o terceiro número: "))

numeros = [num1, num2, num3]
soma = 0
indice = 0

while indice < len(numeros):
    soma += numeros[indice]
    indice += 1
    
print(f"A soma entre {num1}, {num2} e {num3} é igual a {soma}")
