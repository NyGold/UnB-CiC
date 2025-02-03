pop_a, pop_b, taxa_a, taxa_b = ["123", "2000", "2.0", "3.0"]
anos_passados = 0

pop_a = int(pop_a)
pop_b = int(pop_b)

taxa_a = float(taxa_a) / 100
taxa_b = float(taxa_b) / 100

while True:
    anos_passados += 1

    pop_a += int(pop_a * taxa_a)
    pop_b += int(pop_b * taxa_b)

    if pop_a >= pop_b:
        if anos_passados > 1000:
            print("Mais de um milenio")
        else:
            print(f"Alcanca em {anos_passados} ano(s).")
        break