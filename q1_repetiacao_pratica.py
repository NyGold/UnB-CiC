def ieee754(bits, e, m):
    sequencia_expoente = bits[1:e+1]
    sequencia_mantissa = bits[e+1:]

    sinal = (-1)**(int(bits[0]))
    offset = 2**(len(sequencia_expoente) - 1) - 1

    expoente = 0
    contador = len(sequencia_expoente) - 1

    for b in sequencia_expoente:
        expoente += int(b) * 2**(contador)
        contador -= 1

    expo = expoente - offset

    mantissa = 0
    contador = 1

    for b in sequencia_mantissa:
        mantissa += int(b) * 2**((-1) * contador)
        contador += 1

    resultado = sinal * (1. + mantissa) * (2**expo)

    return resultado


print(ieee754('00101000', 3, 4))
print(ieee754('10101000', 3, 4))
print()
print(ieee754('10111111010000000000000000000000', 8, 23))
print(ieee754('01000001010100100000000000000000', 8, 23))
print()
print(ieee754('0100101000000', 3, 9))