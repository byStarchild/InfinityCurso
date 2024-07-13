inicio = int(input("Digite o primeiro número: "))
fim = int(input("Digite o segundo número: "))

soma = 0
par = False

for num in range(inicio, fim + 1):
    if num % 2 == 0:
        soma += num
        par = True
        
print(f"A soma dos números pares de {inicio} a {fim} é:", soma)
        
        




