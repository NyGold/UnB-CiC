ira1, nome1, mes_nascimento1 = input().split()
ira2, nome2, mes_nascimento2 = input().split()

ira1 = float(ira1)
ira2 = float(ira2)

mes_nascimento1 = int(mes_nascimento1)
mes_nascimento2 = int(mes_nascimento2)


def main():
    decisao(ira1, nome1, mes_nascimento1)
    decisao(ira2, nome2, mes_nascimento2)


def decisao(ira, nome, mes_nascimento):
    if ira >= 4:
        if not mes_nascimento == 10:
            # quem tem o maior ira ganha
            if ira > ira2:
                print(nome1)
            elif ira < ira2:
                print(nome2)

            # caso o ira for igual vai pela ordem alfabetica maior
            if ira1 == ira2:
                if nome1[0].lower() < nome2[0].lower():
                    print(nome1)

                elif nome2[0].lower() > nome2[0].lower():
                    print(nome2)
        else:
            print(nome)
    else:
        print(f"{nome}, melhor focar nos estudos.")

main()