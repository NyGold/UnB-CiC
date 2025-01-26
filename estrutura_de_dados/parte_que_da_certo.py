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
    distancia = 0
    i = 0
    
    for c in fila:
        if c == '0':
            distancia = fila[fila.index('0'): fila.index('1')].count('0')
            maior_distancia = distancia if distancia > maior_distancia else maior_distancia
            fila = fila[fila.index(c):]
        else:
            distanica = (fila[fila.index('1'):fila.index('1', fila.index('1'))].count('0') // 2) + 1
            maior_distancia = distancia if distancia > maior_distancia else maior_distancia
            fila = fila[fila.index(c):]

    
print(maior_distancia) 