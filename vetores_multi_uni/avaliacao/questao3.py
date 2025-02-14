# está errada em muito de outros casos

mensagem = input().strip()

def decifrar_mensagem(s):
    # dividir a mensagem em linhas de tamanho 5
    linhas = [s[i:i+5] for i in range(0, len(s), 5)]
    linhas = linhas[::-1]

    # inverter o conteúdo das linhas com índice par
    for i in range(len(linhas)):
        if i % 2 == 0:
            linhas[i] = linhas[i][::-1]

    mensagem_original = ''.join(linhas)

    return mensagem_original.rstrip() # rstrip() retorna a string com os espaços desnecessarios depois removidos

mensagem_decifrada = decifrar_mensagem(mensagem)
print(mensagem_decifrada)