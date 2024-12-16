sequencia = 7 * "0" + 7 * "1"

def vantagem(s):
    if 7*"1" in s and 7*"0" in s:
        print("JOGO PESADO")
        return None
    elif 7*"1" in s:
        print("VAMO TRICOLOR")
        return None
    elif 7*"0" in s:
        print("VAI TIMAO")
        return None
    else:
        print("BORA UM VIRTUAL NO CODEFORCES")

vantagem(sequencia)