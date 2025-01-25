def porta_nor(x,y):
    if not (x == 1 or y == 1):
        return 1
    else:
        return 0


# o que vai para o site
def porta_not(x):
    return porta_nor(x, x)


def porta_e(x, y):
    return porta_nor(porta_not(x), porta_not(y))


def porta_ou(x, y): # 1 se x = 1 ou y = 1
    return porta_not(porta_nor(x,y))


def porta_nand(x, y): # 
    return porta_not(porta_e(x, y))


def porta_xor(x,y):
    # verdadeiro se somente um dos valores for verdadeiro
    return porta_e(porta_not(porta_e(x,y)), porta_ou(x,y))


# testes

print(porta_not(0))
print(porta_not(1))

print(porta_e(0, 0))
print(porta_e(0, 1))
print(porta_e(1, 0))
print(porta_e(1, 1))