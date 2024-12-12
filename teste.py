sequencia = input()

if 7*"1" in sequencia:
    print("VAMO TRICOLOR")

elif 7*"0" in sequencia:
    print("VAI TIMAO")

elif 7*"1" in sequencia and 7*"0" in sequencia:
    print("JOGO PESADO")

else:
    print("BORA UM VIRTUAL NO CODEFORCES")