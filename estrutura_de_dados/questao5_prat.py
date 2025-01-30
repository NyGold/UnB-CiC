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
    distancia = 0

    
    # aqui que vai contar a distancia maxima
    for c in fila: # roda toda a fileira procurando por ocorrencia de 0
        if c == '0':
            distancia = fila[fila.index(c):fila.index('1')].count('0') 
            maior_distancia = distancia if distancia > maior_distancia else maior_distancia                
        else:
            distancia = ( fila[ (fila.index(c)+1) : fila[fila.index(c)+1:].index('1') ].count('0') // 2 ) + 1
            maior_distancia = distancia if distancia > maior_distancia else maior_distancia
        
    maior_distancia = distancia if distancia > maior_distancia else maior_distancia
    
print(maior_distancia) 
