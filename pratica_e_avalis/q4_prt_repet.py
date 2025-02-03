menor_salario = float('inf')
i = 0

while True:
    i += 1
    nome, salario = input().split(",")
    salario = float(salario)

    if nome == "Fim":
        if i > 1:
            print(f"{nome_menor_salario}")
        else:
            print("Não tem")
        break

    nome_menor_salario = nome if salario < menor_salario else nome_menor_salario
    menor_salario = salario if salario < menor_salario else menor_salario