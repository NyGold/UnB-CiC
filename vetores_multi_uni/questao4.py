N, M, f = [int(i) for i in input().split()]
B = [[0] * (M//f) for _ in range(N//f)]

A = []
for _ in range(N):
    A.append([int(x) for x in input().split()])

for _ in range(N//f):
    auxiliar = A[:N//f]
    A = A[N//f:]
    for _ in range(M//f):
        