len_terreno_x, len_terreno_y = [int(i) for i in input().split()]
qtde_bombas = int(input())

profundidade = [[0] * len_terreno_y for _ in range(len_terreno_x)]

'''< o que tinha de problema com o outro código? >

basicamente quando eu criava a matriz profundidade desse jeito:
    profundidade = [[0] * len_terreno_y] * len_terreno_x

o python entendia com esse código que eu queria criar vetores de tamanho
len_terreno_y tantas vezes len_terreno_x, que possuem o mesmo indentificador
entre eles, então quando eu ia referenciar somente um deles, eu acabava alterando
todos com o mesmo indentificador. Ou seja toda a matriz!

Para melhorar a situação, apenas faça ele definir os vetores separados de qualquer
outro jeito. Como o que eu fiz aqui em cima:

profundidade = [[0] * len_terreno_y for _ in range(len_terreno_x)]

ou como meu colega fez:

terreno = []
for i in range(y_terreno):
    linhas = []
    for _ in range(x_terreno):
        linhas.append(0)
    terreno.append(linhas)
'''
for _ in range(qtde_bombas):
    x, y = [int(i) for i in input().split()]

    x -= 1
    y -= 1

    for i in range(len_terreno_y):
        profundidade[x][i] += 1

    for j in range(len_terreno_x):
        profundidade[j][y] += 1

    profundidade[x][y] -= 1

max_profundidade = max(max(linha) for linha in profundidade)
count = sum(linha.count(max_profundidade) for linha in profundidade)
print(count)