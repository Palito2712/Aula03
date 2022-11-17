def listaVazia(tamanho):
    lista = [0] * tamanho
    return lista

lista1 = listaVazia(int(input("Por favor, digite o tamanho da lista: ")))
lista2 = []

for valor in lista1:
    preencherLista = int(input("Digite um valor para preencher a lista: "))
    lista2.append(preencherLista)

print("Essa é a sua lista: ", lista2)
print("Essa é a soma dos valores da sua lista: ", sum(lista2))
print("Esse é o menor valor da sua lista: ", min(lista2))

lista2.reverse()
print("Essa é a sua lista inversa: ", lista2)