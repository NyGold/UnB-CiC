# define a matriz
tamanho_terreno_x, tamanho_terreno_y = [int(i) for i in input().split()]
coodernadas_projetil = []
qtde_projeteis = int(input())

for _ in range(qtde_projeteis):
    coodernadas_projetil.append([int(i) for i in input().split()])

profundidade = [[0] * tamanho_terreno_x] * tamanho_terreno_y

