# Solicita o nome do aluno
nome = input("Digite o nome do aluno: ")

# Inicializa variáveis para as notas
nota1 = 0
nota2 = 0
nota3 = 0

# Coleta as três notas usando um loop for
for i in range(1, 4):
    nota = float(input(f"Digite a nota {i}: "))
    if i == 1:
        nota1 = nota
    elif i == 2:
        nota2 = nota
    elif i == 3:
        nota3 = nota

# Calcula a média das notas
media = (nota1 + nota2 + nota3) / 3

# Exibe a média e o resultado final
print(f"\nNome do aluno: {nome}")
print(f"Média das notas: {media:.2f}")

# Verifica se o aluno foi aprovado ou reprovado
if media >= 7:
    print("O aluno foi aprovado!")
else:
    print("O aluno foi reprovado.")