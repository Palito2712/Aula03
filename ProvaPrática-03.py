matriz = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]
for linha in range(4):
    for coluna in range(4):
        matriz[linha][coluna] = int(input("Por favor, digite um número inteiro: "))

for indice in range(4):
    print(matriz[indice])

menor = matriz[0][0]
numeroImpar = 0

for line in range(4):
    for col in range(4):
        if matriz[line][col] < menor:
            menor = matriz[line][col]
        elif matriz[line][col] %2 != 0:
            numeroImpar += 1

print("O menor valor da matriz é: ", menor)
print("A quantidade de números ímpares é: ", numeroImpar)