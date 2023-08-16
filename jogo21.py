import random

condicao_parada = 21

print("----------------------------------------------")
print("------------------PLAYER----------------------")
print("----------------------------------------------")

while True:
    #Start
    jogo = input("Deseja iniciar? Pressione 'Enter' para Sim [N]ao: ")
    
    #Caso n queira iniciar
    if jogo.upper() == "N":
        print("Parando o jogo...")
        break
    #Se escolher iniciar
    else:
        #Dando as cartas do Host e Player1
        carta_ini = random.randrange(1, 11)
        ply1 = (carta_ini,)
        ply2 = (carta_ini,)
        soma_ply2 = 0
        soma_ply1 = 0
        #jogo iniciado
        while soma_ply1 < condicao_parada:
            num = random.randrange(1, 11)
            
            ply1 += (num,)
            soma_ply1 = sum(ply1)
            print(ply1, " = ", soma_ply1)

            #21 ou valor maior para o player 1
            if soma_ply1 >= 21:
                #se der 21
                if soma_ply1 == 21:
                    print("*--------------*")
                    print("Você Ganhou!!!")
                    print("*--------------*")
                    print(soma_ply1)
                    break
                #Valor superior a 21
                else:
                    print("Você perdeu")
                    print(soma_ply1)
                    break
            
            #Escolher se vai continuar ou parar
            print()
            escolha = input("Escolha [P]arar [C]ontinuar: ")
            
            #Caso continue
            if escolha.upper() == 'C':
                print(f"Número gerado: {num} - Soma parcial: {soma_ply1}")
                if soma_ply1 >= condicao_parada:
                    break
            #Caso decida parar
            elif escolha.upper() == 'P':
                break
            #Outro valor colocado sem ser Continuar ou Parar, vai ser lido Continuar
            else:
                print("Por favor, selecionar apenas P ou C")
                print()
                print()
                print()

        print("----------------------------------------------")
        print("-------------------HOST-----------------------")
        print("----------------------------------------------")
        #Se o Player 1 passou de 21
        if soma_ply1 > 21:
            print("Player perdeu")
            print("Valor Player :: ", soma_ply1)
        else:
            #Senao o Host vai jogar
            while soma_ply2 < condicao_parada:
                print()
                num = random.randrange(1, 11)
                #Cartas do host
                ply2 += (num,)
                soma_ply2 = sum(ply2)
                print(ply2, " = ", soma_ply2)
                #Se o HOST fizer 21 ou valor maior
                if soma_ply2 >= 21:
                    #Se fier 21
                    if soma_ply2 == 21:
                        print("Host Ganhou!!!")
                        print(soma_ply2)
                        break
                    #Se for maior que 21
                    else:
                        print("Host perdeu")
                        print(soma_ply2)
                        break
                #'Sistema' de escolha do Host
                #Se host ficar com menos ou igual de 15 vai sempre continuar
                if soma_ply2 <= 15:
                    escolha = "C"
                #Se for um valor maior como 19 ou 20 vai ser feito um sorteio ou ele para ou continuar
                elif soma_ply2 == 19 or soma_ply2 == 20:
                    #decisao aleatoria se o Player1 tiver 'ganho' a maquina vai decidir se continua ou n
                    if soma_ply1 == 21:
                        escolha = random.choice(["P", "C"])
                    #Se nao a maquina para
                    else:
                        escolha = "P"
                #Se o resultado for diferente de 15 e superior vai ser sorteado a proxima decisao, como 16, 17 e 18
                else:
                    escolha = random.choice(["P", "C"])
                
                #Decisão do Host se vai continuar
                if escolha.upper() == 'C':
                    print(f"Número gerado: {num} - Soma parcial: {soma_ply2}")
                    if soma_ply2 >= condicao_parada:
                        break
                #Decisao do host se vai parar
                elif escolha.upper() == 'P':
                    break
            #Se o host passar de 21
            if soma_ply2 > 21:
                print("Player 1 venceu")
                print("valor do host :: ", soma_ply2)
            #Resultado
            else:
                if soma_ply1 < 21 or soma_ply2 < 21:
                    if soma_ply2 > soma_ply1:
                        print("  Valor Host :: ", soma_ply2 )
                        print('Host venceu')
                        print("Valor Player :: ", soma_ply1)

                    elif soma_ply1 == soma_ply2:
                        print("Valor Player :: ", soma_ply1)
                        print("  Valor Host :: ", soma_ply2 )
                        print('Empate!')

                    else:
                        print("Valor Player :: ", soma_ply1)
                        print("*--------------*")
                        print('Jogador 1 venceu')
                        print("*--------------*")
                        print("  Valor Host :: ", soma_ply2 )
                        
                else:
                    print("Valor Player :: ", soma_ply1 )
                    print("  Valor Host :: ", soma_ply2 )
                    print("Empate!")
