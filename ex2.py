# 2. Crie uma função que recebe uma string e retorna um dicionário com a contagem de cada caractere
# presente na string.

def contaCaractere(string):
    palavraAlt = {}
    for caractere in string:
        if caractere in palavraAlt:
            palavraAlt[caractere] += 1
        else:
            palavraAlt[caractere] = 1

    for caractere, quantidade in palavraAlt.items():
        print(caractere, quantidade)

palavra = input("Digite uma palavra: ")
contaCaractere(palavra)