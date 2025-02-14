x_terreno, y_terreno = input().split()
x_terreno = int(x_terreno)
y_terreno = int(y_terreno)

#mapeano o terreno
terreno = []
for i in range(y_terreno):
    linhas = []
    for _ in range(x_terreno):
        linhas.append(0)
    terreno.append(linhas)


#sistema de bombas
for _ in range(int(input())):
    x,y = input().split()
    x = int(x) - 1
    y = int(y) - 1
    for i in range(x_terreno):
        terreno[y][i] += 1
    for i in range(y_terreno):
        terreno[i][x] += 1
    terreno[y][x] -= 1

for _ in terreno:
    print(_)
'''
#Pegando a quantidade de espaços com maior profundidade
maisFundos = []
a=0
for i in terreno:
    maisFundos.append(max(i))
for c in terreno:
    a+=c.count(max(maisFundos))
print(a)
'''