# define a matriz
tamanho_terreno_x, tamanho_terreno_y = [int(i) for i in input().split()]
coodernadas_projetil = []
qtde_projeteis = int(input())

for _ in range(qtde_projeteis):
    coodernadas_projetil.append([int(i) for i in input().split()])

profundidade = [[0] * tamanho_terreno_x] * tamanho_terreno_y

for bomba in range(qtde_projeteis):
    coodernadas_projetil_x, coodernadas_projetil_y = coodernadas_projetil[bomba]

    coodernadas_projetil_x -= 1
    coodernadas_projetil_y -= 1

    for x in range(tamanho_terreno_x-1):
        profundidade[coodernadas_projetil_x][x] += 1

    for y in range(tamanho_terreno_y-1):
        profundidade[y][coodernadas_projetil_y] += 1


    profundidade[coodernadas_projetil_x-1][coodernadas_projetil_y-1] -= 1

#     y=1 2 3
# x= i  0 1 2
# 1  0 [0 0 0]    x    0       1       2
# 2  1 [0 0 0]    y  0 1 2   0 1 2   0 1 2
# 3  2 [0 0 0]  ou [[0,0,0],[0,0,0],[0,0,0]]

for i in profundidade:
    print(i)