import random

carta_ini = int(random.randrange(1, 11))
ply1 = (carta_ini,)
ply2 = (carta_ini,)

condicao_parada = 21
soma_ply2 = 0
soma_ply1 = 0

print("----------------------------------------------")
print("------------------PLAYER----------------------")
print("----------------------------------------------")
print()
while True:
    jogo = input("Deseja iniciar? [S]im ou [N]ao: ")
    ply1 = (carta_ini,)
    ply2 = (carta_ini,)
    soma_ply2 = 0
    soma_ply1 = 0
    if jogo.upper != "S":
        while soma_ply1 < condicao_parada:
            num = random.randrange(1, 11)
            
            ply1 += (num,)
            soma_ply1 = sum(ply1)
            print(ply1, " = ", soma_ply1)
            
            if soma_ply1 >= 21:
                if soma_ply1 == 21:
                    print("*--------------*")
                    print("Você Ganhou!!!")
                    print("*--------------*")
                    print(soma_ply1)
                    break
                else:
                    print("Você perdeu")
                    print(soma_ply1)
                    break
            
            print()
            escolha = input("Escolha [P]arar [C]ontinuar: ")
            
            if escolha.upper() == 'C':
                print(f"Número gerado: {num} - Soma parcial: {soma_ply1}")
                if soma_ply1 >= condicao_parada:
                    break
            elif escolha.upper() == 'P':
                break
            else:
                print("Por favor, selecionar apenas P ou C")
                print()
                print()
                print()

        print("----------------------------------------------")
        print("-------------------HOST-----------------------")
        print("----------------------------------------------")

        if soma_ply1 > 21:
            print("Jogador 1 perdeu")
        else:
            while soma_ply2 < condicao_parada:
                print()
                num = random.randrange(1, 11)
                
                ply2 += (num,)
                soma_ply2 = sum(ply2)
                print(ply2, " = ", soma_ply2)
                
                if soma_ply2 >= 21:
                    if soma_ply2 == 21:
                        print("Host Ganhou!!!")
                        print(soma_ply2)
                        break
                    else:
                        print("Host perdeu")
                        print(soma_ply2)
                        break
                
                if soma_ply2 < 16:
                    escolha = "C"
                elif soma_ply2 == 19 or soma_ply2 == 20:
                    if soma_ply1 == 21:
                        escolha = random.choice(["P", "C"])
                    else:
                        escolha = "P"
                else:
                    escolha = random.choice(["P", "C"])
                
                if escolha.upper() == 'C':
                    print(f"Número gerado: {num} - Soma parcial: {soma_ply2}")
                    if soma_ply2 >= condicao_parada:
                        break
                elif escolha.upper() == 'P':
                    break

            if soma_ply1 < 21 or soma_ply2 < 21:
                if soma_ply2 > soma_ply1:
                    print('Host venceu')
                elif soma_ply1 == soma_ply2:
                    print('Empate!')
                else:
                    print("*--------------*")
                    print('Jogador 1 venceu')
                    print("*--------------*")
            else:
                print("Empate!")