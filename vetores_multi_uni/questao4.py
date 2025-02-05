def main():
    N, M, f = [int(i) for i in input().split()]

    A = []
    B = [[0] * (M//f) for _ in range(N//f)]
    res = []

    for _ in range(N):
        A.append([int(x) for x in input().split()])

    if N == M == f:
        res = A
        num_max = max(max(linha) for linha in A)
        B.append(num_max)
        return

    for i in range(len(A)//f):
        res.append(A[i][:len(A[0])//f])
        num_max = max(max(linha) for linha in res)
        print(num_max)

main()