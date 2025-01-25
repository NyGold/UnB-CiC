# dentre um número de fileiras e cadeiras, encontre o espaçamento maior
# que alguém possa ficar de outra pessoa já sentada. livre: 0, ocupada: 1

fileiras_e_cadeiras = input().split()
maior_distancia = 0

def str2int(vetor):
    res = []
    
    for e in vetor:
        res.append(int(e))
    return res

fileiras, cadeiras = str2int(fileiras_e_cadeiras)

for f in range(fileiras):
    fila = input().split()
    

    maior_distancia = distancia if distancia > maior_distancia else maior_distancia
    
print(maior_distancia) 