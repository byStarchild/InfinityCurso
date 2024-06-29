import random

numero = random.randint(1, 10)
palpite_restante = 3

print("Vamos jogar um jogo? Tente advinhar o número de 1 a 10")

while palpite_restante > 0:
    palpite = int(input("Palpite {}: Qual é o seu palpite? ".format(4 - palpite_restante)))
    
    if palpite == numero:
        print("Você acertou!")
        break
    else:
        if palpite < numero:
            print("Talvez esteja mais para cima...")
        else:
            print("Talvez esteja mais para baixo...")
            
        palpite_restante -= 1
        print(f"Palpites restantes: {palpite_restante}")

else:
    print(f"Acabaram as chances! O número era {numero}")
    print("Até a próxima")
    
    


