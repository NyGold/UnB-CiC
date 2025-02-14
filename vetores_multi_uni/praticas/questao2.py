num = int(input())
nomes = []
reverso = []

for _ in range(num):
    nome = input()
    nomes.append(nome)

for i in range(1, len(nomes)+1):
    reverso.append(nomes[-i])
    
for e in reverso:
    print(e)