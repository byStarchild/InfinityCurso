##Verificar sexo conforme digitado
Sexo = input("Qual o seu sexo? (F/M):")

if Sexo == "f" or Sexo == "F":
    print("Seu sexo é feminino")
elif Sexo == "m" or Sexo == "M":
    print("Seu sexo é masculino")
else:
    print("Não identificado")

## Verificar se a letra digitada é consoante ou vogal
letra = input("Digite uma letra para verificação: ")

vogais = "aeiouAEIOU"

if letra in vogais:
    print("é uma vogal")
else:
    print("é uma consoante")
    
## Verificar média de notas e aprovar ou reprovar aluno    
num1 = float(input("Digite o valor da primeira nota: "))
num2 = float(input("Digite o valor da segunda nota: "))

resultado = (num1 + num2) / 2

if resultado >= 7:
    print("aprovado")
elif resultado < 7:
    print("reprovado")
elif resultado == 10:
    print("aprovado sem distinção")
