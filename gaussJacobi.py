from normaVetores import norma

def jacobi(A, b, epsilon, iterMax=50):
    n = len(A)
    x = n * [0]

    for k in range(iterMax):
        v = n * [0]
        for i in range(n):
            S = sum(A[i][j] * x[j] for j in range(n) if i != j)
            v[i] = (b[i] - S) / A[i][i]

        d = norma(v, x)
        if d <= epsilon:
            return v

        x = v[:]  # Atualiza o vetor atual

    print("Número máximo de iterações alcançado")
    return x

A = [[10, 2, 1],
     [1, 5, 1],
     [2, 3, 10]]
b = [7, -8, 6]
eps = 0.05
x = jacobi(A, b, eps)
print(x)
