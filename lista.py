# alunos = []
# notas = []

# for i in range(4):
#     pessoas = str(input('Qual o seu nome?: '))
#     alunos.append(pessoas)
    
# for i in range(4):
#     numeros = float(input(f'Digite a nota {i + 1}: '))
#     notas.append(numeros)

# media = numeros/4

# if media >= 6:
#     print('aprovado')
# else:
#     print('reprovado')

# maiorQ = max(notas)

# Listas para armazenar os dados
alunos = []
notas = []

# Captura de dados para 4 usuários
for i in range(4):
    nome = input(f'Qual o nome do aluno {i + 1}?: ')
    alunos.append(nome)
    
    notas_aluno = []
    for j in range(4):
        notas_aluno.append(notas)
    notas.append(notas_aluno)

# Processamento e exibição dos resultados
for i in range(4):
    aluno = alunos[i]
    notas_aluno = notas[i]
    
    # Calcula a média das notas
    media = sum(notas_aluno) / len(notas_aluno)
    
    # Determina se aprovado ou reprovado
    if media >= 6:
        status = 'aprovado'
    else:
        status = 'reprovado'
    
    # Encontra a maior nota
    maior_nota = max(notas_aluno)
    
    # Exibe os resultados
    print(f'\nAluno: {aluno}')
    print(f'Média das notas: {media:.2f}')
    print(f'Situação: {status}')
    print(f'Maior nota: {maior_nota}')