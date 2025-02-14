m, n = [int(i) for i in input().split()]
tabuleiro = [input().strip() for _ in range(n)]

def verificar_vitoria(tabuleiro, m, n):
    # verificar horizontal
    for i in range(n):
        for j in range(m - 3):
            if tabuleiro[i][j] == tabuleiro[i][j+1] == tabuleiro[i][j+2] == tabuleiro[i][j+3] and tabuleiro[i][j] != '.':
                return [tabuleiro[i][j], 'horizontal']

    # verificar vertical
    for j in range(m):
        for i in range(n - 3):
            if tabuleiro[i][j] == tabuleiro[i+1][j] == tabuleiro[i+2][j] == tabuleiro[i+3][j] and tabuleiro[i][j] != '.':
                return [tabuleiro[i][j], 'vertical']

    # verificar diagonal (para baixo e para cima depois desse bloco)
    for i in range(n - 3):
        for j in range(m - 3):
            if tabuleiro[i][j] == tabuleiro[i+1][j+1] == tabuleiro[i+2][j+2] == tabuleiro[i+3][j+3] and tabuleiro[i][j] != '.':
                return [tabuleiro[i][j], 'diagonal']

    for i in range(3, n):
        for j in range(m - 3):
            if tabuleiro[i][j] == tabuleiro[i-1][j+1] == tabuleiro[i-2][j+2] == tabuleiro[i-3][j+3] and tabuleiro[i][j] != '.':
                return [tabuleiro[i][j], 'diagonal']

    return

vencedor, direcao = verificar_vitoria(tabuleiro, m, n)

if vencedor == 'V':
    print('Vermelho na', direcao)
else:
    print('Azul na', direcao)