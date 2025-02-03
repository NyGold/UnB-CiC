a, b, c = input("a, b, c: ").split()

a = int(a)
b = int(b)
c = int(c)

# código que vai para o site
def classificador(a, b, c):
    e_triangulo = ((a + b) > c) and ((b + c) > a)

    if not e_triangulo: 
        print("gondim sendo gondim")
        return None

    print ("triangulo")

    if (a != b) and (a != c) and (b != c):
        print("escaleno")

    if (a == b) or (b == c) or (a == c):
        print("isosceles")

    if (a == b) and (b == c):
        print("equilatero")

    if (a >= b) or (b >= c): # a é o maior lado
        if a**2 == ((b**2) + (c**2)):
            print("retangulo")

    if (b >= a) or (a >= c): # b é o maior lado
        if b**2 == ((a**2) + (c**2)):
            print("retangulo")

    if (c >= b) or (b >= a): # c é o maior lado
        if c**2 == ((a**2) + (b**2)):
            print("retangulo")


classificador(a,b,c)