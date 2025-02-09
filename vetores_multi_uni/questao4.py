N, M, f = [int(i) for i in input().split()]
B = [[0] * (M//f) for _ in range(N//f)]

A = [[int(i) for i in input().split()] for _ in range(N)]

for i in range(N // f):
    for j in range(M // f):
        # Encontrar o máximo na região atual
        max_val = -1
        for x in range(f):
            for y in range(f):
                linha = i * f + x
                coluna = j * f + y
                max_val = A[linha][coluna] if A[linha][coluna] > max_val else max_val

        B[i][j] = max_val

for linha in B:
    print(*linha)