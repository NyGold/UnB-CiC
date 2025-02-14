def soma_matriz(matrizes):
    m1 = matrizes[0]
    m2 = matrizes[1]
    res = m1
    # computar a soma de matrizes
    for i in range(len(res)):
        for j in range(len(res[0])):
            res[i][j] += m2[i][j]
    # aprensentar os resultados
    for i in res:
        print(*i)

matriz = [[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]
soma_matriz(matriz)