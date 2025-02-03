# codigo que vai para o site
def porta_e(x, y):
    return 1 if (x == 1 and y == 1) else 0

def porta_ou(x, y):
    return 1 if (x == 1 or y == 1) else 0

def porta_not(x):
    if x == 1:
        return 0
    else:
        return 1

def porta_nand(x, y):
    return porta_not(porta_ou(x, y))

def porta_nor(x, y):
    return porta_not(porta_ou(x, y))

def porta_xor(x, y):
    return 0 if x == y else 1

# testes
print(porta_e(0, 0))
print(porta_e(0, 1))
print(porta_e(1, 0))
print(porta_e(1, 1))
