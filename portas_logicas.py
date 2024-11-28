vb1 = input()
vb2 = input()

# codigo que vai para o site
def porta_not(vb):
    return not vb

def porta_nand(vb1, vb2):
    if not (vb1 == 1 and vb2 == 1):
        return 0

print(porta_nand())
print(porta_not())
