# 1. Crie uma função que recebe uma lista de números inteiros e retorna uma nova lista contendo apenas os
# números pares.

def filtraPares(lista):
    return [num for num in lista if num % 2 == 0]

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Números pares: ", filtraPares(numeros))