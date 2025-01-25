num1 = int(input())
num2 = int(input())
num3 = int(input())

operacao = input().lower()

if operacao != "p" and operacao != "h" and operacao != "a":
    print("Operacao inexistente")

if operacao == 'p':
    peso1 = int(input())
    peso2 = int(input())
    peso3 = int(input())

    media = peso1*num1 + peso2*num2 + peso3*num3
    media = media / (peso1 + peso2 + peso3)

    print(f"Ponderada: {media:.2f}")

if operacao == 'a':
    media = num1 + num2 + num3
    media = media / 3

    print(f"Aritmetica: {media:.2f}")

if operacao == 'h':
    media = 3 / (1/num1 + 1/num2 + 1/num3)

    print(f"Harmonica: {media:.2f}")