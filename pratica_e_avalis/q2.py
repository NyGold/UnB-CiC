palindromo = input()

qtd_letras_diferentes = 0
metade_indice = (len(palindromo) - 1) // 2

if len(palindromo) % 2 == 0:
    for i in palindromo[:metade_indice + 1]:
        for j in palindromo[metade_indice + 1:]:
            if i != j:
                qtd_letras_diferentes += 1


elif len(palindromo) % 2 != 0:
# gl x lg mtd = 5 // 2 -> 2
# 01 2 34

    qtd_letras_diferentes += 1

    for i in palindromo[:metade_indice]:
        for j in palindromo[metade_indice + 1:]:
            if i != j:
                qtd_letras_diferentes += 1

 
if qtd_letras_diferentes == 1:
    print("ON")
else:
    print("OFF")