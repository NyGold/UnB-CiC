def decodificar_strings(strings):
    resultados = []

    for string in strings:
        decodificada = ""
        i = 0

        while i < len(string):
            # Captura o caractere
            caractere = string[i]
            i += 1

            numero = ""
            while i < len(string) and string[i].isdigit():
                numero += string[i]
                i += 1

            # Expande o caractere com base no número
            decodificada += caractere * int(numero)
        resultados.append(decodificada)

    return resultados


n = int(input())

strings_codificadas = [input().strip() for _ in range(n)]
strings_decodificadas = decodificar_strings(strings_codificadas)

for resultado in strings_decodificadas:
    print(resultado)