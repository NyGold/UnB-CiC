vb1 = int(input())
vb2 = int(input())

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

print(f"vb1 = {vb1}, vb2 = {vb2}")

print()

print(f"porta e: {porta_e(vb1, vb2)}")
print(f"porta ou: {porta_ou(vb1, vb2)}")
print(f"porta not: p/ vb1: {porta_not(vb1)} p/ vb2: {porta_not(vb2)}")
print(f"porta nand: {porta_nand(vb1, vb2)}")
print(f"porta nor: {porta_nor(vb1, vb2)}")
print(f"porta xor: {porta_xor(vb1, vb2)}")
