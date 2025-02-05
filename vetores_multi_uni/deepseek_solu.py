def main():
    # Leitura das dimensões do terreno
    N, M = [int(i) for i in input().split()]

    # Inicialização da matriz de profundidades
    profundidade = [[0] * M for _ in range(N)]

    # Leitura do número de projéteis
    Q = int(input())

    # Processamento dos projéteis
    for _ in range(Q):
        x, y = [int(i) for i in input().split()]
        
        x -= 1  # Ajustando para índice 0-based
        y -= 1  # Ajustando para índice 0-based

        # Incrementa a profundidade na linha x e na coluna y
        for i in range(M):
            profundidade[x][i] += 1
        for j in range(N):
            if j != x:  # Evita incrementar duas vezes a posição (x, y)
                profundidade[j][y] += 1

    # Encontrar a maior profundidade
    max_profundidade = max(map(max, profundidade))

    # Contar quantas posições têm a maior profundidade
    count = sum(row.count(max_profundidade) for row in profundidade)

    # Saída do resultado
    print(count)

if __name__ == "__main__":
    main()