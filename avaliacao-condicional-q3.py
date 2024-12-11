ira1, nome1, mes_nascimento1 = input().split()
ira2, nome2, mes_nascimento2 = input().split()

ira1 = float(ira1)
ira2 = float(ira2)

mes_nascimento1 = int(mes_nascimento1)
mes_nascimento2 = int(mes_nascimento2)

def verificar(ira, nome, mes_nascimento):
    if ira1 < 4 and ira2 < 4:
        return False

    if ira < 4:
        print(f"{nome}, melhor focar nos estudos.")
        return True

    if mes_nascimento1 == 10 and mes_nascimento2 == 10:
        print("Nao posso decidir!")
        return False

    if mes_nascimento == 10:
        print(nome)
    elif ira >= 4:
        return True


if verificar(ira1, nome1, mes_nascimento1) and verificar(ira2, nome2, mes_nascimento2):
    if ira1 > ira2:
        print(nome1)
    elif ira1 < ira2:
        print(nome2)

    if ira1 == ira2:
        if nome1 > nome2:
            print(nome1)
        elif nome1 < nome2:
            print(nome2)
        elif nome1 == nome2:
            print("Nao posso decidir!")
elif ira1 < 4 and ira2 < 4:
    print(f"{nome1} e {nome2}, melhor focarem nos estudos.")