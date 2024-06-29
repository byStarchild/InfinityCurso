#numeros impares

#for i in range(1, 50, 2):
#    print(i)
    
#numero maior e menor dos tres

#num1 = float(input("Digite o primeiro numero: "))
#num2 = float(input("Digite o segundo numero: "))    
#num3 = float(input("Digite o terceiro numero: "))

#menor_numero = num1
#maior_numero = num1

#numeros = [num1, num2, num3]

#or num in numeros:
#    if num < menor_numero:
#        menor_numero = num
#    if num > maior_numero:
#        maior_numero = num
        
#print(f"o maior número é {maior_numero}")
#print(f"o menor número é {menor_numero}")   

#Pesquisa de preço

preco_banana = float(input("Qual o preço da Banana?: "))
preco_laranja = float(input("Qual o preço da Laranja?: "))
preco_mamão = float(input("Qual o preço do Mamão?: "))

menor_preco = preco_banana
produto_mais_barato = "Banana"

produtos = [("Banana", preco_banana), ("Laranja", preco_laranja), ("Mamão", preco_mamão)]

for nome, preco in produtos:
    if preco < menor_preco:
        menor_preco = preco
        produto_mais_barato = nome

print(f"Produto com menor preço:{produto_mais_barato}, está custando R${menor_preco}")