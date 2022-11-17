#Profe, infelizmente eu me perdi no meio do código e não consegui finalizar, ficou incompleto.
#A ideia eu sei qual é, mas não consegui executar. Desculpas prof.

import random

dado = [1, 2, 3, 4, 5, 6]
listaPlayer1 = []
listaPlayer2 = []

decisao = input("Você gostaria de jogar o dado? ")

while decisao:
    decisao = decisao.strip().upper()
    numero = random.choice(dado)

    if(decisao == "SIM"):
        print("O número que caiu para o Player 1 foi: ", numero)
        listaPlayer1.append(numero)

        decisao = input("Deseja jogar novamente (SIM OU NÃO)? ").upper()
        listaPlayer2.append(numero)
    elif(decisao == "NÃO" or decisao =="NAO"):
        break

    else:
        print("Digite apenas SIM ou NÃO....")
        decisao = input("Deseja jogar novamente (SIM OU NÃO)? ").upper()

if decisao == "NÃO" or decisao == "NAO":
    print("Fim de Jogo! Volte Logo...")

    print("Soma dos valores do Player 1: ", sum(listaPlayer1))
    print("Soma dos valores do Player 2: ", sum(listaPlayer2))
    print("O número de jogadas do Player 1 foi: ", listaPlayer1[-1])
    print("O número de jogadas do Player 2 foi: ", listaPlayer2[-1])

if sum(listaPlayer1) > sum(listaPlayer2):
    print("O Player 1 venceu!!")

if sum(listaPlayer1) < sum(listaPlayer2):
    print("O Player 2 venceu!!")