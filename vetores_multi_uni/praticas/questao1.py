num_jogadores = int(input())
jogadores = []

for _ in range(num_jogadores):
    jogador = input()
    jogadores.append(jogador)

impostores = input().split()

for i in jogadores :
    for j in impostores:
        if j in jogadores:
            jogadores.remove(j)

print(*jogadores)