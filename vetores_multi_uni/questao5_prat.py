def valor_max_fileira(f):
    cadeiras_vazias = []
    
    for i in f:
        cadeiras_vazias.append(i.count("0"))

    for i in range(1, len(cadeiras_vazias)-1):
        cadeiras_vazias[i] = (cadeiras_vazias[i] + 1) // 2
         
    return max(cadeiras_vazias)


n, m = [int(i) for i in input().split()]
valores_max = []

for _ in range(n):
    fileira = input()
    fileira = fileira.replace(" ", "")
    fileira = fileira.split("1")
    
    valores_max.append(valor_max_fileira(fileira))
    
print(max(valores_max))
