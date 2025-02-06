N, M, f = [int(i) for i in input().split()]
B = [[0] * (M//f) for _ in range(N//f)]
part1 = []
part2 = []
part3 = []
part4 = []

A = []
for _ in range(N):
    A.append([int(x) for x in input().split()])

indices_revert = [i for i in range(-(len(A)//2),0)]
indices_revert.sort(reverse=True)

print("\nMatriz A:")
for i in A:
    print(i)

if N == f:
    num_max =  max(max(linha) for linha in A)
    print(num_max)
else:
    for i in range(len(A)//2):
        part1.append(A[i][:len(A[0])//2])
        part2.append(A[i][len(A[0])//2:])

    for i in indices_revert:
        part3.append(A[i][:len(A[0])//2])
        part4.append(A[i][len(A[0])//2:])

    print("\nparte 1 de A:")
    for i in part1:
        print(i)

    print("\nparte 2 de A:")
    for i in part2:
        print(i)

    print("\nparte 3 de A:")
    for i in part3:
        print(i)

    print("\nparte 4 de A:")
    for i in part4:
        print(i)