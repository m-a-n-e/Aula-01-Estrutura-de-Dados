# 4. Crie uma função que recebe uma lista vazia e permite ao usuário adicionar 5 elementos a essa lista. Ao
# final, a função deve retornar a lista completa.

def addLista(lista):
    for i in range(5):
        elemento = input(f"Digite o elemento de número {i + 1}: ")
        lista.append(elemento)
    return lista

elementos = []
addLista(elementos)
print(elementos)