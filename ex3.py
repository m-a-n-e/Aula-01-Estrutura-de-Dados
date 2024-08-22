# 3. Crie uma função que recebe um dicionário onde as chaves são nomes de alunos e os valores são listas
# com suas notas. A função deve calcular a média das notas de cada aluno e retornar um novo dicionário
# com os nomes e suas respectivas médias.

def calculaMedia(dados):
    medias = {}
    for nome, notas in dados.items():
            media = sum(notas) / len(notas)
            medias[nome] = media
    return medias

dadosAlunos = {'Letícia': [8, 9, 6, 7.2], 'Emanuel': [9, 8.5, 2, 10], 'Pedro': [1, 8.1, 5, 9], 'João': [6, 8.2, 6, 7]}

print(calculaMedia(dadosAlunos))